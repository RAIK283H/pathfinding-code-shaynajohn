import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())
    

def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    #precondition: that the target node is not empty
    assert len(global_game_data.target_node) > 0, "Target node list is empty."
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    #precondition: that the graph is not empty
    assert len(graph) > 0, "The graph is empty."
    start_node = 0
    exit_node = len(graph) - 1
    path = []
    
    target = global_game_data.target_node[global_game_data.current_graph_index]
    current_node = start_node
    path.append(current_node)

    #second requirement: not allowing player to return to the starting node
    can_return_to_start = False
    visited_target = False

    while current_node != exit_node:
        neighbors_list = graph[current_node][1]

        if target in neighbors_list and not visited_target:
            next_node = target
            visited_target = True

        elif not can_return_to_start and start_node in neighbors_list:
            neighbors_list.remove(start_node) # for the second requirement
            next_node = random.choice(neighbors_list)
        
        elif not visited_target:
            next_node = target
            visited_target = True

        else:
            next_node = random.choice(neighbors_list)

        path.append(next_node)
        current_node = next_node

    #post condition: the path has more than 3 elements. must include the start node, target node, exit node
    assert len(path) >= 3, "Path must contain at least three nodes."
    #post condition: the starting node was only visited once
    assert path.count(start_node) <= 1, "The starting node was visited more than once."
    return path

def validating_path(graph, path, target, exit_node):
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]

        if next_node not in graph[current_node][1]:
            return False  
    
    if target not in path:
        return False
    
    if path[-1] != exit_node:
        return False
    
    return True 

def random_generation():
    visited_nodes = []
    visited_nodes.add()



def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]

get_random_path()