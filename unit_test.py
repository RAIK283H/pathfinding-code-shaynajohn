import math
import unittest
import pathing
import main_two
import permutation
import f_w
import global_game_data


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)


    def test_valid_path_includes_target(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]
        
        path = [0, 1, 3] 
        target = 1
        exit_node = 3
        result = pathing.validating_path(test_graph, path, target, exit_node)
        self.assertTrue(result)


    def test_empty_path(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [] 
        target = 1
        exit_node = 3
        result = pathing.validating_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_target_not_in_path(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 2, 3]  
        target = 1
        exit_node = 3
        result = pathing.validating_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_all_nodes_in_path_are_adjacent(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 1, 3] 
        exit_node = 3
        target = 1
        result = pathing.validating_path(test_graph, path, target, exit_node)
        self.assertTrue(result)

    def test_nodes_in_path_are_not_adjacent(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 2, 1] 
        exit_node = 3
        target = 1
        result = pathing.validating_path(test_graph, path, target, exit_node)

        self.assertFalse(result)

    def test_path_does_no_exit_node(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 2] 
        target = 1
        exit_node = 3
        result = pathing.validating_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_no_valid_neighbors(self):
        test_graph = [
            [0, []], #no neighbors 
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 3]
        target = 1
        exit_node = 3
        result = pathing.validating_path(test_graph, path, target, exit_node)
        self.assertFalse(result) 

    def test_dfs_path_includes_target(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]

        path = [0, 1, 3]
        target = 1
        exit_node = 3
        result = pathing.validating_dfs_path(test_graph, path, target, exit_node)
        self.assertTrue(result)

    def test_dfs_empty_path(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [] 
        target = 1
        exit_node = 3
        result = pathing.validating_dfs_path(test_graph, path, target, exit_node)
        self.assertFalse(result)


    def test_dfs_no_target(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 2, 3]  
        target = 1
        exit_node = 3
        result = pathing.validating_dfs_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_all_nodes_in_path_are_adjacent_dfs(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 1, 3] 
        exit_node = 3
        target = 1
        result = pathing.validating_dfs_path(test_graph, path, target, exit_node)
        self.assertTrue(result)

    def test_nodes_in_path_are_not_adjacent_dfs(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 2, 1] 
        exit_node = 3
        target = 1
        result = pathing.validating_dfs_path(test_graph, path, target, exit_node)

        self.assertFalse(result)

    def test_path_does_no_exit_node_dfs(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 2] 
        target = 1
        exit_node = 3
        result = pathing.validating_dfs_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_no_valid_neighbors_dfs(self):
        test_graph = [
            [0, []], #no neighbors 
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 3]
        target = 1
        exit_node = 3
        result = pathing.validating_dfs_path(test_graph, path, target, exit_node)
        self.assertFalse(result) 

    def test_bfs_path_includes_target(self):
            test_graph = [
                [0, [1, 2]],
                [1, [0, 3]],
                [2, [0, 3]],
                [3, [1, 2]]
            ]

            path = [0, 1, 3]
            target = 1
            exit_node = 3
            result = pathing.validating_bfs_path(test_graph, path, target, exit_node)
            self.assertTrue(result)

    def test_bfs_empty_path(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [] 
        target = 1
        exit_node = 3
        result = pathing.validating_bfs_path(test_graph, path, target, exit_node)
        self.assertFalse(result)


    def test_bfs_no_target(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 2, 3]  
        target = 1
        exit_node = 3
        result = pathing.validating_bfs_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_all_nodes_in_path_are_adjacent_bfs(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 1, 3] 
        exit_node = 3
        target = 1
        result = pathing.validating_bfs_path(test_graph, path, target, exit_node)
        self.assertTrue(result)

    def test_nodes_in_path_are_not_adjacent_bfs(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 2, 1] 
        exit_node = 3
        target = 1
        result = pathing.validating_bfs_path(test_graph, path, target, exit_node)

        self.assertFalse(result)

    def test_path_does_no_exit_node_bfs(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 2] 
        target = 1
        exit_node = 3
        result = pathing.validating_bfs_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_no_valid_neighbors_bfs(self):
        test_graph = [
            [0, []], #no neighbors 
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 3]
        target = 1
        exit_node = 3
        result = pathing.validating_bfs_path(test_graph, path, target, exit_node)
        self.assertFalse(result) 


    def test_permutations(self):
        n = 3
        perms = permutation.permutations(n)
        expected_permutations = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2]
        ]

        self.assertCountEqual(perms, expected_permutations)

    def test_empty_permutation(self):
        n = 0
        perms = permutation.permutations(n)
        self.assertEqual(perms, [[]])

    def test_permutationn(self):
        n = 2
        perms = permutation.permutations(n)
        expected_permuations = [
            [1, 2],
            [2, 1]
        ]
        self.assertCountEqual(perms, expected_permuations)

    def test_single_element_permutation(self):
        n = 1
        perms = permutation.permutations(n)
        self.assertEqual(perms, [[1]]) 
    
    def test_valid_hamiltonian_cycle(self):
        graph = [
            [(0, 0), [1, 3]],  
            [(1, 0), [0, 2]],  
            [(1, 1), [1, 3]],  
            [(0, 1), [0, 2]]  
        ]
        path = [0, 1, 2, 3, 0]
        self.assertTrue(main_two.check_hamiltonian_cycle(graph, path)[0])

    def test_invalid_hamiltonian_cycle(self):
        graph = [
            [(0, 0), [1]],      
            [(1, 0), [0, 2]],  
            [(1, 1), [1, 3]],  
            [(0, 1), [5]]      
        ]
        path = [0, 1, 2, 3, 0]
        self.assertFalse(main_two.check_hamiltonian_cycle(graph, path)[0])

    def test_not_hamiltonian(self):
        graph = [
            [(0, 0), [1, 2]],   
            [(1, 0), [0, 2]],   
            [(1, 1), [0, 1]]    
        ]
        path = [0, 1, 2]  
        self.assertFalse(main_two.check_hamiltonian_cycle(graph, path)[0])

    def test_multiple_edges(self):
        graph = [
            [(0, 0), [1, 1]],  
            [(1, 0), [0, 2, 2]],  
            [(1, 1), [1, 3]],  
            [(0, 1), [2, 0]]    
        ]
        path = [0, 1, 2, 3, 0]
        self.assertTrue(main_two.check_hamiltonian_cycle(graph, path)[0])


    def test_no_edges_graph(self):
        graph = [
            [(0, 0), []],  
            [(1, 1), []],  
            [(0, 1), []]   
        ]
        path = [0, 1, 2, 0]
        self.assertFalse(main_two.check_hamiltonian_cycle(graph, path)[0])

    def test_only_one_node(self):
        graph = [
            [(0, 0), [0,0]]  
        ]
        path = [0, 0]  
        self.assertTrue(main_two.check_hamiltonian_cycle(graph, path)[0])

    def test_dijkstra_path_includes_target(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]

        path = [0, 1, 3]
        target = 1
        exit_node = 3
        result = pathing.validating_dijkstra_path(test_graph, path, target, exit_node)
        self.assertTrue(result)

    def test_dijkstra_empty_path(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [] 
        target = 1
        exit_node = 3
        result = pathing.validating_dijkstra_path(test_graph, path, target, exit_node)
        self.assertFalse(result)


    def test_dijkstra_no_target(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 2, 3]  
        target = 1
        exit_node = 3
        result = pathing.validating_dijkstra_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_adjacent_dijkstra(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 1, 3] 
        exit_node = 3
        target = 1
        result = pathing.validating_dijkstra_path(test_graph, path, target, exit_node)
        self.assertTrue(result)

    def test_nodes_not_adjacent_dijkstra(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 2, 1] 
        exit_node = 3
        target = 1
        result = pathing.validating_dijkstra_path(test_graph, path, target, exit_node)

        self.assertFalse(result)

    def test_path_no_exit_node_dijkstra(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 2] 
        target = 1
        exit_node = 3
        result = pathing.validating_dijkstra_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_no_valid_neighbors_dijkstra(self):
        test_graph = [
            [0, []], 
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 3]
        target = 1
        exit_node = 3
        result = pathing.validating_dijkstra_path(test_graph, path, target, exit_node)
        self.assertFalse(result) 


    def test_astar_path_includes_target(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]

        path = [0, 1, 3]
        target = 1
        exit_node = 3
        result = pathing.validating_astar_path(test_graph, path, target, exit_node)
        self.assertTrue(result)

    def test_astar_empty_path(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [] 
        target = 1
        exit_node = 3
        result = pathing.validating_astar_path(test_graph, path, target, exit_node)
        self.assertFalse(result)


    def test_astar_no_target(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 2, 3]  
        target = 1
        exit_node = 3
        result = pathing.validating_astar_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_adjacent_astar(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 1, 3] 
        exit_node = 3
        target = 1
        result = pathing.validating_astar_path(test_graph, path, target, exit_node)
        self.assertTrue(result)

    def test_nodes_not_adjacent_astar(self):
        test_graph = [
            [0, [1, 2]],   
            [1, [0, 3]],   
            [2, [0, 3]],   
            [3, [1, 2]]    
        ]

        path = [0, 2, 1] 
        exit_node = 3
        target = 1
        result = pathing.validating_astar_path(test_graph, path, target, exit_node)

        self.assertFalse(result)

    def test_path_no_exit_node_astar(self):
        test_graph = [
            [0, [1, 2]],
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 2] 
        target = 1
        exit_node = 3
        result = pathing.validating_astar_path(test_graph, path, target, exit_node)
        self.assertFalse(result)

    def test_no_valid_neighbors_astar(self):
        test_graph = [
            [0, []], 
            [1, [0, 3]],
            [2, [0, 3]],
            [3, [1, 2]]
        ]
        
        path = [0, 1, 3]
        target = 1
        exit_node = 3
        result = pathing.validating_astar_path(test_graph, path, target, exit_node)
        self.assertFalse(result) 



    def test_no_edges(self):
        graph_data = [
            [], [], []
        ]
        n = 3
        expected_dist = [
            [0, math.inf, math.inf],
            [math.inf, 0, math.inf],
            [math.inf, math.inf, 0]
        ]
        
        dist, parent = f_w.floyd_warshall(graph_data, n)
        self.assertEqual(dist, expected_dist)

    
    def test_build_path(self):
        parent = [
            [None, 0, 1],
            [1, None, 1],
            [1, 2, None]
        ]
        start, end = 0, 2
        expected_path = [0,0, 1, 2]
        result_path = f_w.build_path(parent, start, end)
        self.assertEqual(result_path, expected_path)

    def test_build_path_no_path(self):
        parent = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        start = 0
        end = 2
        expected_path = [0, 2]  
        
        result = f_w.build_path(parent, start, end)
        self.assertEqual(result, expected_path)

    def test_build_path_hamiltonian(self):
        parent = [
            [None, 0, 1],
            [None, 0, 1],
            [None, None, None]
        ]
        start = 0
        end = 0
        expected_path = [0,0]
        
        result = f_w.build_path(parent, start, end)
        self.assertEqual(result, expected_path)


    def test_generate_adjacency_matrix(self):
        graph_data = [
            [(1, [1,2])],  
            [(1, [0])],     
            [(1, [0])]     
        ]
        nodes = 3
        expected_matrix = [
            [0, 1, 1],
            [1, 0, math.inf], 
            [1, math.inf, 0]   
        ]
        
        result = f_w.generate_adjacency_matrix(graph_data, nodes)
        self.assertEqual(result, expected_matrix)

    def test_generate_adjacency_matrix_empty_graph(self):
        graph_data = [[], [], []]
        nodes = 3
        expected_matrix = [
            [0, math.inf, math.inf],  
            [math.inf, 0, math.inf],
            [math.inf, math.inf, 0]
        ]
        
        result = f_w.generate_adjacency_matrix(graph_data, nodes)
        self.assertEqual(result, expected_matrix)

    def test_generate_adjacency_matrix_single_node(self):
        graph_data = [[]]  
        nodes = 1
        expected_matrix = [
            [0] 
        ]
        
        result = f_w.generate_adjacency_matrix(graph_data, nodes)
        self.assertEqual(result, expected_matrix)

    def test_generate_adjacency_matrix_disconnected_graph(self):
        graph_data = [
            [(1, [1])],  
            [],          
            [(1, [0])]   
        ]
        nodes = 3
        expected_matrix = [
            [0, 1, math.inf],
            [math.inf, 0, math.inf],
            [1, math.inf, 0]
        ]
        
        result = f_w.generate_adjacency_matrix(graph_data, nodes)
        self.assertEqual(result, expected_matrix)



    def test_floyd_warshall_compare_dijkstra_graph1(self):
        graph_data = [
            [(3, [1])],      
            [(4, [2])],      
            [(5, [0])]        
        ]
        n = 3

        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)

        fw_path = paths[start_node][end_node]
        
        self.assertEqual(fw_path, dj_path)


    def test_floyd_warshall_compare_dijkstra_graph3(self):
        graph_data = [
            [(1, [1])],      
            [(1, [2])],       
            [(5, [0])]        
        ]
        n = 3

        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)

        fw_path = paths[start_node][end_node]
        
        self.assertEqual(fw_path, dj_path)

    def test_floyd_warshall_compare_dijkstra_more_weights(self):
        graph_data = [
            [(2, [1])],       
            [(3, [2])],      
            [(10, [0])]       
        ]
        n = 3

        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)

        fw_path = paths[start_node][end_node]
        
        self.assertEqual(fw_path, dj_path)
 
    def test_floyd_warshall_compare_dijkstra_high_weight(self):
        graph_data = [
            [(3, [1])],       
            [(1, [2])],       
            [(100, [0])]     
        ]
        n = 3

        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)

        fw_path = paths[start_node][end_node]
        
        self.assertEqual(fw_path, dj_path)

    def test_floyd_warshall_compare_dijkstra2(self):
        graph_data = [
            [(1, [1])],            
            [(200, [0, 2])],      
            [(1, [1])]             
        ]
        
        n = 3
        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)
  
        fw_path = paths[start_node][end_node]

        self.assertEqual(fw_path, dj_path)  
 
    def test_floyd_warshall_compare_dijkstra3(self):
        graph_data = [
            [(1, [1])],           
            [(500, [0, 2])],      
            [(1, [1])]            
        ]
        
        n = 3
        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)
        
        fw_path = paths[start_node][end_node]
        self.assertEqual(fw_path, dj_path)

    def test_floyd_warshall_compare_dijkstra4(self):
        graph_data = [
            [(3, [1])],          
            [(2, [2])],         
            [(None, [])]         
        ]
        
        n = 3
        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)
        
        fw_path = paths[start_node][end_node]
        self.assertEqual(fw_path, dj_path)


    def test_floyd_warshall_compare_dijkstra5(self):
        graph_data = [
            [(10, [1])],        
            [(5, [2])],          
            [(None, [])]         
        ]
        
        n = 3
        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)
        
        fw_path = paths[start_node][end_node]
        self.assertEqual(fw_path, dj_path)

    def test_floyd_warshall_compare_dijkstra6(self):
        graph_data = [
            [(4, [1])],          
            [(3, [2])],        
            [(None, [])]        
        ]
        
        n = 3
        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)
        
        fw_path = paths[start_node][end_node]
        self.assertEqual(fw_path, dj_path)

    def test_floyd_warshall_compare_dijkstra8(self):
        graph_data = [
            [(5, [1])],         
            [(5, [2])],          
            [(None, [])]        
        ]
        
        n = 3
        start_node = 0
        end_node = 2

        dist, paths = f_w.floyd_warshall(graph_data, n)
        dj_path = pathing.get_dijkstra_path(graph_data, start_node, n, end_node)
        
        fw_path = paths[start_node][end_node]
        self.assertEqual(fw_path, dj_path)


if __name__ == '__main__':
    unittest.main()
