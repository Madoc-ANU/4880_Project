from sklearn.metrics.pairwise import cosine_similarity
from collections import deque
import networkx as nx
import numpy as np


# Function to get distance between two nodes by their names
def get_distance(node1, node2, dist_arg):
    node_index = dist_arg[0]
    matrix = dist_arg[1]
    if node1 not in node_index or node2 not in node_index:
        return None  # Return None if either node doesn't exist
    index1 = node_index[node1]
    index2 = node_index[node2]
    return matrix[index1, index2]
    

# Degree based search
def degree_based_search(G, start, end):
    # Early exit if start is the same as end
    if start == end:
        return [start]
    
    if start not in G or end not in G:
        return None  # Return None if either node doesn't exist

    # Initialize a queue for BFS
    queue = deque([(start, [start])])
    # Set to keep track of visited nodes
    visited = set([start])

    while queue:
        # Pop the first element in the queue
        current_node, path = queue.popleft()

        # Get neighbors and sort them based on degree (descending order)
        neighbors = sorted(G.neighbors(current_node), key=G.degree, reverse=True)

        for neighbor in neighbors:
            if neighbor == end:
                return path + [end]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # If no path is found


#Simlarity Based Search
def similarity_based_search(G, start, end, cosine_sim_matrix, node_index):
    # Early exit if start is the same as end
    if start == end:
        return [start]

    if start not in G or end not in G:
        return None  # Return None if either node doesn't exist

    # Initialize a queue for BFS
    queue = deque([(start, [start])])
    # Set to keep track of visited nodes
    visited = set([start])

    while queue:
        # Pop the first element in the queue
        current_node, path = queue.popleft()

        # Get neighbors and sort them based on similarity to the end node (descending order)
        end_index = node_index[end]
        neighbors = sorted(G.neighbors(current_node), key=lambda x: cosine_sim_matrix[node_index[x], end_index], reverse=True)

        for neighbor in neighbors:
            if neighbor == end:
                return path + [end]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # If no path is found

# random based search
def random_search(G, start, end):
    # Early exit if start is the same as end
    if start == end:
        return [start]
    
    if start not in G or end not in G:
        return None  # Return None if either node doesn't exist

    # Initialize a queue for BFS
    queue = deque([(start, [start])])
    # Set to keep track of visited nodes
    visited = set([start])

    while queue:
        # Pop the first element in the queue
        current_node, path = queue.popleft()

        # Get neighbors and sort them based on degree (descending order)
        neighbors = sorted(G.neighbors(current_node), key=G.degree, reverse=True)
        random.shuffle(neighbors)

        for neighbor in neighbors:
            if neighbor == end:
                return path + [end]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # If no path is found
