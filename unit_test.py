import math
import unittest
import pathing


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


if __name__ == '__main__':
    unittest.main()
