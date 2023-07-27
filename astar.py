def heuristic_distance(a, b):
    # Calculate the Manhattan distance between two points
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(graph, start, goal):
    open_list = [(0, start)]
    closed_set = set()

    while open_list:
        current_cost, current_node = min(open_list)
        open_list.remove((current_cost, current_node))

        if current_node == goal:
            return current_cost

        closed_set.add(current_node)

        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_pos = (current_node[0] + neighbor[0], current_node[1] + neighbor[1])

            if neighbor_pos in graph and neighbor_pos not in closed_set:
                neighbor_cost = current_cost + 1 + heuristic_distance(neighbor_pos, goal)
                open_list.append((neighbor_cost, neighbor_pos))

    return None  # No path found

# Example usage:
if __name__ == "__main__":
    graph = {(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0)}  # Replace this with your own graph
    start = (0, 0)
    goal = (2, 2)

    shortest_distance = astar(graph, start, goal)
    if shortest_distance is not None:
        print("Shortest distance:", shortest_distance)
    else:
        print("No path found.")
