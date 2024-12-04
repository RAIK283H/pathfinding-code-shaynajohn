import math
import graph_data
import global_game_data

def generate_adjacency_matrix(graph_data, nodes):
    infinity = math.inf
    matrix = []

    for i in range(nodes):
        row = []  
        for j in range(nodes):
            row.append(infinity)  
        matrix.append(row)  
    
    for i in range(nodes):
        matrix[i][i] = 0  
    
    for i in range(nodes):
        edges = graph_data[i]

        for edge in edges:
            weight = 1  
            neighbors = edge[1]  

            for neighbor in neighbors:
                matrix[i][neighbor] = weight  
    
    return matrix


def floyd_warshall(graph_data, nodes):
    infinity = float('inf')
    
    dist = []
    path = []
    
    for i in range(nodes):
        row = []
        for j in range(nodes):
            row.append(infinity)
        dist.append(row)
    
    for i in range(nodes):
        row = []
        for j in range(nodes):
            row.append(None)
        path.append(row)

    for i in range(nodes):
        dist[i][i] = 0
        for weight, neighbors in graph_data[i]:
            for neighbor in neighbors:
                dist[i][neighbor] = 1  
                path[i][neighbor] = [i, neighbor]
    
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[i][k][:-1] + path[k][j]

    return dist, path


def build_path(parent, start, end):
    path = []
    current = parent[start][end]

    while current is not None:  
        path.insert(0, current)  
        current = parent[start][current]
    
    path.insert(0, start)  
    path.append(end)      

    return path


#fw player for extra credit
def get_fw_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    nodes = len(graph)
    start_node = 0
    exit_node = len(graph) - 1
    target = global_game_data.target_node[global_game_data.current_graph_index]

    dist = []
    path = []
    infinity = float('inf')

    for i in range(nodes):
        row = []
        for j in range(nodes):
            row.append(infinity)
        dist.append(row)

    for i in range(nodes):
        row = []
        for j in range(nodes):
            row.append(None)
        path.append(row)

    for i in range(nodes):
        dist[i][i] = 0
        for neighbor in graph[i][1]:
            dist[i][neighbor] = 1  
            path[i][neighbor] = [i, neighbor]
       

    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[i][k][:-1] + path[k][j]


    path_to_target = []
    if path[start_node][target] is not None:
        path_to_target = path[start_node][target]


    path_from_target = []
    if path[target][exit_node] is not None:
        path_from_target = path[target][exit_node]

    path_to_target.pop()  
    full_path = path_to_target + path_from_target

    # post condition: the path has more than 3 elements. must include the start node, target node, exit node
    assert len(full_path) >= 3, "Path must contain at least three nodes."
    # post condition: that the target was visited
    assert full_path.__contains__(target), "Target was not visited."
    # post condition: that the exit node was last node visited
    assert full_path[-1] == exit_node, "Last node is not the exit node."
    # post condition: that the start node was the first node visited
    assert full_path[0] == start_node, "Start node is not the first node."

    return full_path
