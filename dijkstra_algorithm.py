import numpy as np
import heapq

# Graph represented as adjacency matrix
graph = [ 
    [0,3,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,0,3,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,3,0,5,2,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,5,0,5,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,2,5,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,5,0,0,0,0,3,0,3,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,5,4,0,3,0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,4,0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,2,0,0,2,3,3,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,2,0,0,0,5,4,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,0,0,3,0,0,1,0,0,4,0,0,0,2,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,3,0,1,0,3,0,0,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,5,0,3,0,2,0,0,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,4,0,0,2,0,0,0,0,5,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3,0,0,0,4,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,2,0,0,3,0,4,0,0,0,5,2,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,4,0,4,0,0,0,1,4,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,4,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,3,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,1,0,2,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,2,0,3,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3,0,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3,0]
]
# Reliability matrix
reliability = [
    [0.0,0.97,0.0,0.0,0.0,0.98,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.97,0.0,0.96,0.0,0.0,0.99,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.96,0.0,0.98,0.95,0.0,0.97,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.98,0.0,0.95,0.0,0.98,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.95,0.95,0.0,0.0,0.0,0.95,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.98,0.99,0.0,0.0,0.0,0.0,0.96,0.0,0.99,0.0,0.98,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.97,0.98,0.0,0.96,0.0,0.99,0.96,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.95,0.0,0.99,0.0,0.0,0.96,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.99,0.96,0.0,0.0,0.97,0.95,0.98,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.96,0.97,0.0,0.0,0.0,0.98,0.95,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.98,0.0,0.0,0.95,0.0,0.0,0.97,0.0,0.0,0.97,0.0,0.0,0.0,0.95,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.98,0.0,0.97,0.0,0.96,0.0,0.0,0.99,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.98,0.0,0.96,0.0,0.97,0.0,0.0,0.96,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.95,0.0,0.0,0.97,0.0,0.0,0.0,0.0,0.98,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.97,0.0,0.0,0.0,0.0,0.96,0.0,0.0,0.0,0.97,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.99,0.0,0.0,0.96,0.0,0.98,0.0,0.0,0.0,0.95,0.98,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.96,0.0,0.0,0.98,0.0,0.98,0.0,0.0,0.0,0.95,0.95,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.98,0.0,0.0,0.98,0.0,0.0,0.0,0.0,0.0,0.0,0.96],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.95,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.96,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.97,0.0,0.0,0.0,0.96,0.0,0.96,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.95,0.0,0.0,0.0,0.96,0.0,0.96,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.98,0.95,0.0,0.0,0.0,0.96,0.0,0.97,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.95,0.0,0.0,0.0,0.0,0.97,0.0,0.95],
[ 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.96,0.0,0.0,0.0,0.0,0.95,0.0]
]
# Capacity matrix
capacity = [
    [0,10,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[10,0,7,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,7,0,5,7,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,5,0,5,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,7,5,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[4,3,0,0,0,0,10,0,3,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,4,10,0,10,0,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,6,0,9,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,3,9,0,0,9,8,10,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,9,9,0,0,0,8,4,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,8,0,0,8,0,0,8,0,0,5,0,0,0,9,0,0,0,0,0],
[0,0,0,0,0,0,0,0,10,0,8,0,7,0,0,4,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,8,0,7,0,10,0,0,8,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,4,0,0,10,0,0,0,0,3,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,9,0,0,0,4,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,4,0,0,9,0,5,0,0,0,10,10,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,5,0,10,0,0,0,10,3,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,10,0,0,0,0,0,0,5],
[0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,5,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,5,0,4,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,4,0,9,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,10,0,0,0,9,0,10,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,10,0,6],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,6,0]
]
# Delay matrix
delay = [
    [0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[2,0,4,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,4,0,3,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,3,0,3,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,2,3,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[2,1,0,0,0,0,2,0,1,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,4,0,2,0,5,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,4,0,5,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,2,0,0,2,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,3,2,0,0,0,4,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,4,0,0,5,0,0,2,0,0,4,0,0,0,3,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,2,0,5,0,0,3,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,4,0,5,0,1,0,0,5,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,4,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,5,0,0,0,2,2,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,5,0,1,0,0,0,3,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,1,0,0,0,0,0,0,2],
[0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,4,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,4,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1,0,5,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,0,0,0,5,0,4,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,4,0,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0]

]

# Set thresholds for the constraints
bandwidth_demand = 5
delay_threshold = 40
reliability_threshold = 0.70

# Get start and end vertices from the user
while True:
    start = int(input("Enter start vertex (0-23): "))
    if 0 <= start < len(graph):
        break

while True:
    end = int(input("Enter end vertex (0-23): "))
    if 0 <= end < len(graph):
        break

# Dijkstra's algorithm
dist = [float("inf")] * len(graph)
dist[start] = 0
heap = [(0, start)]
path = {}

while heap:
    curr_dist, curr_vert = heapq.heappop(heap)

    if curr_vert == end:
        break

    for neighbor, weight in enumerate(graph[curr_vert]):
        if (
            weight != 0
            and dist[neighbor] > dist[curr_vert] + weight
            and capacity[curr_vert][neighbor] >= bandwidth_demand
            and delay[curr_vert][neighbor] < delay_threshold
            and reliability[curr_vert][neighbor] > reliability_threshold
        ):
            dist[neighbor] = dist[curr_vert] + weight
            path[neighbor] = (curr_vert, weight)  # Store the predecessor and edge weight
            heapq.heappush(heap, (dist[neighbor], neighbor))

# Check if the final path satisfies the conditions
shortest_path = [end]
prev, total_capacity, total_reliability, total_delay = end, 0, 1.0, 0

while prev != start:
    prev, weight = path[prev]
    total_capacity += capacity[prev][shortest_path[-1]]
    total_reliability *= reliability[prev][shortest_path[-1]]
    total_delay += delay[prev][shortest_path[-1]]
    shortest_path.append(prev)

shortest_path.reverse()

# Print the final path if it satisfies all the conditions
if (
    total_capacity >= bandwidth_demand
    and total_delay < delay_threshold
    and total_reliability > reliability_threshold
):
    print("Shortest path:", shortest_path)
    print("Shortest distance:", dist[end])
    print("Total capacity along the path:", total_capacity)
    print("Total reliability along the path:", total_reliability)
    print("Total delay along the path:", total_delay)
    print("The solution according to the objective function:", dist[end] * bandwidth_demand)
else:
    print("No path satisfies the conditions found.")



    #  This code is implementation of Dijkstra's algorithm that gives you the shortest path between two input from 0 to 23 that also satisfies some conditions