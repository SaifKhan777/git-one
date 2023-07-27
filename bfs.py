from collections import deque

def bfs(graph, start_node, target_node):
    visited = set()
    queue = deque([(start_node, [])])  # (current_node, path_taken)

    while queue:
        current_node, path_taken = queue.popleft()

        if current_node == target_node:
            return path_taken

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                queue.append((neighbor, path_taken + [neighbor]))

    return None

# Example usage:
# Assume the graph is represented as a dictionary where keys are nodes and values are lists of neighbors.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

start_node = 'A'
target_node = 'F'
shortest_path = bfs(graph, start_node, target_node)
print("Shortest path:", shortest_path)
