# calculate total resistance between two nodes in a simple resistor network
# file format: node1, node2, resistance

# we use a graph and dijkstra to find the shortest path (lowest resistance)

import heapq

def read_network(filename):
    graph = {}

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue
            node1 = int(parts[0].strip())
            node2 = int(parts[1].strip())
            resistance = float(parts[2].strip())

            # add edges in both directions (undirected)
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append((node2, resistance))
            graph[node2].append((node1, resistance))

    return graph

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            return current_distance

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return float('inf')  # if no path found

# main
if __name__ == "__main__":
    # choose your file here: small or large
    filename = "smallResNetwork.txt"
    graph = read_network(filename)

    # choose start and end node (can be changed if needed)
    start_node = 9
    end_node = 25

    result = dijkstra(graph, start_node, end_node)

    if result != float('inf'):
        print(f"total resistance from node {start_node} to {end_node}: {result} kΩ")
    else:
        print("no connection between nodes")
