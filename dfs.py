def dfs(graph, current_node, target_node, visited=set(), path=[]):
    if current_node == target_node:
        path.append(current_node)
        print("Path found:", path)
        return True

    if current_node not in visited:
        visited.add(current_node)
        path.append(current_node)

        for neighbor in graph[current_node]:
            if dfs(graph, neighbor, target_node, visited, path):
                return True

        path.pop()

    return False

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
dfs(graph, start_node, target_node)
