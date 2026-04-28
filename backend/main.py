import os
import csv
import heapq
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# --- DATA MODELS ---
class RouteRequest(BaseModel):
    start: str
    end: str

class StepModel(BaseModel):
    step: int
    type: str # 'start', 'middle', 'end'
    location: str

class RouteResponse(BaseModel):
    start: str
    end: str
    distance: float
    estimated_minutes: int
    path: List[str]
    steps: List[StepModel]

# --- GRAPH & ALGORITHM LOGIC ---
def build_graph(csv_path):
    """Loads map edges from CSV and creates an adjacency list."""
    graph = {}
    if not os.path.exists(csv_path):
        return {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            u, v, w = row['source'], row['destination'], float(row['distance'])
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
            # Bidirectional campus roads
            graph[u].append((v, w))
            graph[v].append((u, w))
    return graph

def dijkstra(graph, start, end):
    """Calculates shortest path using Dijkstra's algorithm."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    prev = {node: None for node in graph}

    while pq:
        current_distance, u = heapq.heappop(pq)
        if current_distance > distances[u]: continue
        if u == end: break

        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                prev[v] = u
                heapq.heappush(pq, (distances[v], v))

    path = []
    curr = end
    while curr:
        path.append(curr)
        curr = prev[curr]
    return distances[end], path[::-1]

# --- API SERVER ---
app = FastAPI(title="TIET Campus Navigation API")

# Enable CORS for communication with the React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from the CSV file (located in the root as requested)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "tiet_campus_map.csv")
graph = build_graph(DATA_PATH)

@app.get("/locations")
async def get_locations():
    """Returns a sorted list of all campus landmarks."""
    return sorted(list(graph.keys()))

@app.post("/shortest-path", response_model=RouteResponse)
async def get_shortest_path(request: RouteRequest):
    """Calculates and returns the shortest path between two points."""
    start, end = request.start, request.end

    if start not in graph or end not in graph:
        raise HTTPException(status_code=404, detail="Location not found.")
    
    if start == end:
        raise HTTPException(status_code=400, detail="Start and End points are identical.")

    distance, path = dijkstra(graph, start, end)

    if distance == float('inf'):
        raise HTTPException(status_code=404, detail="No route found.")

    # Create UI-friendly steps for the navigator
    steps = [StepModel(step=i, location=loc, type="middle") for i, loc in enumerate(path)]
    steps[0].type = "start"
    steps[-1].type = "end"

    return RouteResponse(
        start=start, end=end,
        distance=distance,
        estimated_minutes=max(1, int(distance // 80)),
        path=path,
        steps=steps
    )

if __name__ == "__main__":
    import uvicorn
    # Start the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
