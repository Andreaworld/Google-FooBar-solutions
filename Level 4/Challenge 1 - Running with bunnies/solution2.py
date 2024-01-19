"""
This problem is similar to the traveling salesman problem but with two crucial differences:
    1. You can repeat visiting nodes
    2. There are negative weights to some links
    3. This is a directed graph
    4. The solution is which nodes can be visited given a cost limit (that can be violated 
        due to point 2), not the cost of the minimun path

For point 4, this program will go through all the combinations of possible answers and using 
an intermediate result so that solving the traveling salesman problem for the intermediate
result can be tested against the cost limit to see if this attempted possible answer is valid.

Putting aside negative cycles, if we calculate the shortest path for all pairs of nodes, this
solves the other three points. For point 1, we desire to reach each node at least once, and 
if the cost of visiting each node directly is the cheapest cost, there is no need to revisit
any node. For point 2 and 3, the brute force approach to the problem isn't affected by negative
weights (assuming no negative cycles) or the graph being directed, so it doesn't matter.

If there is a negative cycle, before we apply the the traveling salesman algorithm, we check
if, for any of the nodes, the cost of traveling to itself after calculating the shortest path
for all pairs of nodes is negative, then we just return every bunny.

If no possible answer was found to be valid, we just return an empty list.
"""
from itertools import combinations



def solution(times, times_limit):
    # Number of bunnies being attempted to save
    number_of_bunnies = len(times) - 2

    # Helper variables
    start = 0 # The starting node index
    bulkhead = len(times) - 1 # index of the bulkhead

    # Keep trying to save as many bunnies as possible
    while number_of_bunnies > 1:
        # Different possible solutions for saving this many bunnies
        combination_of_bunnies = list(combinations(range(1, bulkhead), number_of_bunnies))

        # Try each combination
        for bunnies_to_rescue in combination_of_bunnies:
            # apsp - all pairs shortest paths
            apsp = shortest_paths(times, [start] + list(bunnies_to_rescue) + [bulkhead])

            # If this is every bunny, check if negative cycle exists
            if number_of_bunnies == len(times)-2:
                if any(apsp[i][i] for i in range(number_of_bunnies+2)):
                    # Negative cycle exists, return trivial solution
                    return reformat(bunnies_to_rescue)

            # Check if answer is valid
            if tsp(apsp) <= times_limit:
                # This is the solution
                return reformat(bunnies_to_rescue)
        
        # Can't save this many bunnies, try one less
        number_of_bunnies -= 1
    
    # No bunnies can be saved, just save yourself
    return []


# Helper function
def reformat(unformatted_solution):
    # Map lambda function to convert the index numbering of the
    # bunnies to the id numbering
    return map(lambda x: x-1, list(unformatted_solution))


# brute force recursive with memo Traveling Salesman solver 
def tsp(distance_matrix):
    # Get the number of nodes in the graph
    num_nodes = len(distance_matrix)
    
    # Create a set of all nodes
    all_nodes = set(range(num_nodes))
    
    # Initialize memoisation dictionary
    memo = {}
    
    # Helper function to solve the TSP problem recursively
    def tsp_helper(curr_node, remaining_nodes):
        # Base case: If there are no remaining nodes to visit,
        # return the distance from the current node to the last node
        if len(remaining_nodes) == 0:
            return distance_matrix[curr_node][num_nodes - 1]

        # Create a key for memoization based on the current node and remaining nodes
        memo_key = (curr_node, tuple(remaining_nodes))
        
        # Check if the subproblem has already been solved and return the stored result
        if memo_key in memo:
            return memo[memo_key]

        # Initialize the minimum distance to a large value
        min_distance = float('inf')

        # Iterate over all remaining nodes
        for next_node in remaining_nodes:
            # Remove the next node from the remaining set
            updated_remaining = remaining_nodes - {next_node}
            
            # Calculate the distance from the current node to the next node
            distance = distance_matrix[curr_node][next_node] + tsp_helper(next_node, updated_remaining)
            
            # Update the minimum distance if the calculated distance is smaller
            min_distance = min(min_distance, distance)

        # Store the minimum distance for the current subproblem in the memoization dictionary
        memo[memo_key] = min_distance
        
        # Return the minimum distance
        return min_distance

    # Call the helper function to solve the TSP problem starting from node 0,
    # excluding the start and end nodes from the remaining set
    optimal_distance = tsp_helper(0, all_nodes - {0, num_nodes - 1})
    
    # Return the optimal distance
    return optimal_distance


def shortest_paths(distance_matrix, nodes):
    n = len(nodes)
    
    # Create a copy of the distance matrix for the specified nodes
    shortest = [[distance_matrix[i][j] for j in nodes] for i in nodes]
    
    # Apply the Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                shortest[i][j] = min(shortest[i][j], shortest[i][k] + shortest[k][j])
    
    return shortest



if __name__ == "__main__":
    print solution([[0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1], 
                    [1, 1, 0, 1, 1], 
                    [1, 1, 1, 0, 1], 
                    [1, 1, 1, 1, 0]], 3)
    
    print solution([[0, 2, 2, 2, -1],
                    [9, 0, 2, 2, -1],
                    [9, 3, 0, 2, -1],
                    [9, 3, 2, 0, -1],
                    [9, 3, 2, 2,  0]], 1)

    print solution([[0, 3, 2, 4],
                    [1, 0, 6, 2],
                    [2, 3, 0, 1],
                    [1, 5, 4, 0]], 7)
    
    print solution([[   0,     2,    5, 9999, 9999, 9999, 9999],
                    [9999,     0,    3, 9999, 9999, 9999, 9999],
                    [9999,  9999,    0,    2,    6, 5000, 9999],
                    [9999,  9999, 9999,    0, 9999,    4,    1],
                    [9999,  9999, 9999,    7,    0, 9999, 9999],
                    [9999, -9999, 9999, 9999, 9999,    0, 9999],
                    [9999,  9999, 9999, 9999, 9999, 9999,    0]], -99)
