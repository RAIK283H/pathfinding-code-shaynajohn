import graph_data
from permutation import permutations
import math


def distance(nodeOne, nodeTwo):
    x1 = nodeOne[0]
    y1 = nodeOne[1]
    x2 = nodeTwo[0]
    y2 = nodeTwo[1]

    distance_formula = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance_formula


def check_hamiltonian_cycle(graph, path):
    current_node = path[0]
    total_distance = 0

    for i in range(1, len(path)):
        next_node = path[i]
        if next_node not in graph[current_node][1]: 
            return False, 0  
        
        #distance between current node to next node
        total_distance += distance(graph[current_node][0], graph[next_node][0])
        current_node = next_node

    #distance between current node back to starting node
    total_distance += distance(graph[current_node][0], graph[path[0]][0])
    
    if path[-1] == path[0]:
        return True, total_distance 
    else:
        return False, 0  


def find_hamiltonians_from_perms(graph):
    n = len(graph)
    all_permutations = permutations(n - 1)
    valid_cycles = []
    min_distance = float('inf')  
    optimal_cycles = []  

    for perm in all_permutations:
        cycle = [0] + perm + [0]
        outcome = check_hamiltonian_cycle(graph, cycle)

        validity = outcome[0]
        distance = outcome [1]

        #if hamiltonian cycle
        if validity == True:
            valid_cycles.append(cycle)
            if distance < min_distance:
                min_distance = distance
                #if min distance is less, clear optimal cycles and add it
                optimal_cycles.clear()
                optimal_cycles.append(cycle)
            # if min distance is =, there is a tie, add both to optimal cycles
            elif distance == min_distance:
                optimal_cycles.append(cycle)  

    if valid_cycles:
        return valid_cycles, optimal_cycles
    else:
        return -1, []  

def print_cycles(graph, index):
    final_outcome = find_hamiltonians_from_perms(graph)
    cycles = final_outcome[0]
    optimal_cycles = final_outcome[1]
    print(f"Graph {index}")

    if cycles == -1:
        print("No valid Hamiltonian cycles found :(.")
    else:
        for cycle in cycles:
            print(cycle)

        if optimal_cycles:
            print("Optimal Hamiltonian cycles:")
            for optimal in optimal_cycles:
                print(optimal)

if __name__ == '__main__':
    import graph_data  
    graph_list = graph_data.graph_data
    graph_count = len(graph_list)

    for i in range(graph_count):
        current_graph = graph_list[i]
        print_cycles(current_graph, i)