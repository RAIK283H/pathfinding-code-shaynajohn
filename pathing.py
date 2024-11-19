import graph_data
import global_game_data
from numpy import random
import heapq
import math

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    #global_game_data.graph_paths.append(get_random_path())
    #global_game_data.graph_paths.append(get_dfs_path())
   # global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())
    global_game_data.graph_paths.append(get_astar_path())
    
    
    

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
    #precondition: that the target node is not empty
    assert len(global_game_data.target_node) > 0, "Target node list is empty."
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    #precondition: that the graph is not empty
    assert len(graph) > 0, "The graph is empty."
    
    start_node = 0
    exit_node = len(graph) - 1
    path = []
    target = global_game_data.target_node[global_game_data.current_graph_index]

    stack = [start_node] 
    visited = set()    

    while stack:
        current_node = stack.pop()
        if current_node in visited:
            continue  
        
        path.append(current_node)
        visited.add(current_node)   

        if current_node == exit_node:
            break  

        for neighbor in graph[current_node][1]:
            if neighbor not in visited:
                stack.append(neighbor)

        if target not in visited:
            stack.append(target)


    #post condition: the path has more than 3 elements. must include the start node, target node, exit node
    assert len(path) >= 3, "Path must contain at least three nodes."
    #post condition: that the target was visited
    assert path.__contains__(target), "Target was not visited."
    #post condition: that the exit node was last node visited
    assert path[-1] == exit_node, "Last node is not the exit node."
    

    return path

#for postcondition checking every pair of sequential vertices in the path are connected by an edge
def validating_dfs_path(graph, path, target, exit_node):
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
  
def get_bfs_path():
   
   #precondition: that the target node is not empty
    assert len(global_game_data.target_node) > 0, "Target node list is empty."
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    #precondition: that the graph is not empty
    assert len(graph) > 0, "The graph is empty."

    start_node = 0
    exit_node = len(graph) - 1
    target = global_game_data.target_node[global_game_data.current_graph_index]

    queue = [start_node] 
    visited = set()
    visited.add(start_node)
    parents = {} 

    while queue:
        current_node = queue.pop() 
        if current_node == exit_node:
            path = []
            while current_node is not None:
                path.insert(0, current_node) 
                current_node = parents.get(current_node)
            return path

        for neighbor in graph[current_node][1]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current_node  
                queue.insert(0, neighbor)  

        if target not in visited:
            visited.add(target)
            parents[target] = current_node
            queue.insert(0, target)  

    #post condition: the path has more than 3 elements. must include the start node, target node, exit node
    assert len(path) >= 3, "Path must contain at least three nodes."
    #post condition: that the target was visited
    assert path.__contains__(target), "Target was not visited."
    #post condition: that the exit node was last node visited
    assert path[-1] == exit_node, "Last node is not the exit node."
    
    return []

def validating_bfs_path(graph, path, target, exit_node):
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

def get_dijkstra_path():
    #precondition: that the target node is not empty
    assert len(global_game_data.target_node) > 0, "Target node list is empty."
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    #precondition: that the graph is not empty
    assert len(graph) > 0, "The graph is empty."

    start_node = 0
    exit_node = len(graph) - 1
    target = global_game_data.target_node[global_game_data.current_graph_index]

    #path from the start to the target
    distances = []
    for i in range(len(graph)):
        distances.append(float('inf'))

    distances[start_node] = 0
    parents = []
    for i in range(len(graph)):
        parents.append(None)

    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))
    visited_nodes = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == target:
            break

        if current_node in visited_nodes:
            continue
        visited_nodes.add(current_node)

        for neighbor in graph[current_node][1]:
            weight = 1
            alt = current_distance + weight
            if neighbor not in visited_nodes and alt < distances[neighbor]:
                distances[neighbor] = alt
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (alt, neighbor))

    path_to_target = []
    current_node = target
    while current_node is not None:
        path_to_target.insert(0, current_node)
        current_node = parents[current_node]

    #path from the target to the end
    distances = []
    for i in range(len(graph)):
        distances.append(float('inf'))

    distances[target] = 0
    
    parents = []
    for i in range(len(graph)):
        parents.append(None)

    priority_queue = []
    heapq.heappush(priority_queue, (0, target))

    visited_nodes.clear()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == exit_node:
            break

        if current_node in visited_nodes:
            continue
        visited_nodes.add(current_node)
        for neighbor in graph[current_node][1]:
            weight = 1
            alt = current_distance + weight
            if neighbor not in visited_nodes and alt < distances[neighbor]:
                distances[neighbor] = alt
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (alt, neighbor))

    path_from_target = []
    current_node = exit_node
    while current_node is not None:
        path_from_target.insert(0, current_node)
        current_node = parents[current_node]

    path_to_target.pop()  
    full_path = path_to_target + path_from_target

    #post condition: the path has more than 3 elements. must include the start node, target node, exit node
    assert len(full_path) >= 3, "Path must contain at least three nodes."
    #post condition: that the target was visited
    assert full_path.__contains__(target), "Target was not visited."
    #post condition: that the exit node was last node visited
    assert full_path[-1] == exit_node, "Last node is not the exit node."
    ##post condition: that the start node was the first node visited
    assert full_path[0] == start_node, "Start node is not the first node."

    return full_path
#for postcondition checking every pair of sequential vertices in the path are connected by an edge
def validating_dijkstra_path(graph, path, target, exit_node):
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

#extra credit
def get_astar_path():
    # precondition: that the target node is not empty
    assert len(global_game_data.target_node) > 0, "Target node list is empty."
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    # precondition: that the graph is not empty
    assert len(graph) > 0, "The graph is empty."

    start_node = 0
    exit_node = len(graph) - 1
    target = global_game_data.target_node[global_game_data.current_graph_index]

    # path from start to target
    costs = []
    for i in range(len(graph)):
        costs.append(float('inf'))
    costs[start_node] = 0

    parents = []
    for i in range(len(graph)):
        parents.append(None)

    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))
    visited_nodes = set()

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node == target:
            break

        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)
        for neighbor in graph[current_node][1]:
            weight = 1
            alt = current_cost + weight
            if neighbor not in visited_nodes and alt < costs[neighbor]:
                costs[neighbor] = alt
                current_cost = alt + heuristic(neighbor, target)
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (current_cost, neighbor))
                
    path_to_target = []
    current_node = target
    while current_node is not None:
        path_to_target.insert(0, current_node)
        current_node = parents[current_node]

    # path from target to end
    costs = []
    for i in range(len(graph)):
        costs.append(float('inf'))
    costs[target] = 0

    parents = []
    for i in range(len(graph)):
        parents.append(None)

    priority_queue = []
    heapq.heappush(priority_queue, (0, target))
    visited_nodes.clear()

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node == exit_node:
            break

        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)
        for neighbor in graph[current_node][1]:
            weight = 1
            alt = current_cost + weight
            if neighbor not in visited_nodes and alt < costs[neighbor]:
                costs[neighbor] = alt
                current_cost = alt + heuristic(neighbor, target)
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (current_cost, neighbor))
                

    path_from_target = []
    current_node = exit_node
    while current_node is not None:
        path_from_target.insert(0, current_node)
        current_node = parents[current_node]

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

def heuristic(node, target):
   return abs(node - target)

def validating_astar_path(graph, path, target, exit_node):
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














