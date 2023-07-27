from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    queue = deque([(0, 0, [])])  # (jug1, jug2, actions)
    visited = set()

    while queue:
        jug1, jug2, actions = queue.popleft()
        state = (jug1, jug2)

        if jug1 == target_amount or jug2 == target_amount:
            return actions

        if state not in visited:
            visited.add(state)
            possible_actions = [
                ("fill_jug1", jug1_capacity, jug2),
                ("fill_jug2", jug1, jug2_capacity),
                ("empty_jug1", 0, jug2),
                ("empty_jug2", jug1, 0),
                ("pour_jug1_to_jug2", jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
                ("pour_jug2_to_jug1", jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))
            ]

            for action, new_jug1, new_jug2 in possible_actions:
                queue.append((new_jug1, new_jug2, actions + [action]))

    return None

# Example usage:
jug1_capacity = 5
jug2_capacity = 3
target_amount = 4
solution = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
print(solution)
