from itertools import permutations

def solution(times, times_limit):
    num_vertices = len(times)
    start_vertex = 0  # Index of the start vertex
    end_vertex = num_vertices - 1  # Index of the end vertex

    # Check if it is possible to gain time unbounded
    can_gain_time_unbounded = False
    for vertex in range(num_vertices):
        if any(weight < 0 for weight in times[vertex]):
            stack = [vertex]
            print times, "hey"
            print stack, "hey"
            visited = set()
            while stack:
                current_vertex = stack.pop()
                visited.add(current_vertex)
                for neighbor, weight in enumerate(times[current_vertex]):
                    if neighbor == vertex and current_vertex != start_vertex:  # Detected a path that returns to the original vertex
                        can_gain_time_unbounded = True
                        break
                    if neighbor not in visited:
                        stack.append(neighbor)
                if can_gain_time_unbounded:
                    break
        if can_gain_time_unbounded:
            break

    # If it is possible to gain time unbounded, return the list of all intermediate vertices
    if can_gain_time_unbounded:
        return list(range(1, num_vertices - 1))

    # Check if a regular tour is possible without ignoring any vertices
    regular_tour = [start_vertex] + list(range(1, num_vertices - 1)) + [end_vertex]
    regular_weight = sum(times[i][j] for i, j in zip(regular_tour[:-1], regular_tour[1:]))

    if regular_weight <= times_limit:
        return [regular_tour]

    possible_tours = []

    # Find tours by ignoring vertices
    for i in range(1, num_vertices - 1):
        # Generate permutations by ignoring i number of vertices
        ignored_vertices_permutations = permutations(range(1, num_vertices - 1), i)

        for ignored_permutation in ignored_vertices_permutations:
            visited_vertices = [start_vertex] + list(ignored_permutation) + [end_vertex]  # Build the tour
            current_weight = 0  # Initialize the current edge weight sum

            # Check if the tour is valid within the weight limit
            for j in range(len(visited_vertices) - 1):
                current_vertex = visited_vertices[j]
                next_vertex = visited_vertices[j + 1]
                edge_weight = times[current_vertex][next_vertex]  # Weight of the edge from current_vertex to next_vertex

                current_weight += edge_weight

                # Allow visiting nodes repeatedly if it means passing a negative weight
                if current_weight >= 0 and current_weight > times_limit:
                    break

            if current_weight <= times_limit:
                possible_tours.append(visited_vertices)

        # If we found any tours by ignoring i number of vertices, return them
        if possible_tours:
            return possible_tours

    return []  # Return an empty list if no tour is found





if __name__ == "__main__":
    print solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
    print solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)

    print solution([[0, 3, 2, 4], [1, 0, 6, 2], [2, 3, 0, 1], [1, 5, 4, 0]], 7)
