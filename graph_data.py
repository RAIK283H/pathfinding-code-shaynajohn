'''
graph_data[a] = gives you graph at index a
graph_data[a][0] = start node of graph a
graph_data[a][length-1] = exit node of graph a
graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
graph_data[a][b][1] = adjacency list of point b in graph a

Only the start and exit nodes are dead ends (all other nodes have degree >= 2)
'''

graph_data = [

    [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1]]
    ],
    [
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
    ],
    [
        [(900, 45), [17, 21, 22]],
        [(70, 350), [2, 7, 19, 20]],
        [(140, 420), [1, 5, 9, 10, 20]],
        [(210, 70), [6, 8, 11, 22]],
        [(210, 210), [6, 7, 11, 12, 20]],
        [(210, 490), [2, 10, 21]],
        [(280, 140), [3, 4, 11, 20]],
        [(280, 280), [1, 4, 9, 12, 20]],
        [(350, 70), [3, 11]],
        [(350, 350), [2, 7, 10, 12, 13, 15]],
        [(350, 490), [2, 5, 9, 13, 14, 15]],
        [(420, 140), [3, 4, 6, 8, 12, 16, 17]],
        [(420, 280), [4, 7, 9, 11, 15, 17]],
        [(420, 420), [9, 10, 15]],
        [(490, 490), [10, 18, 15]],
        [(560, 420), [9, 10, 12, 13, 14, 17, 18]],
        [(630, 70), [11, 17]],
        [(630, 210), [11, 12, 15, 16, 18, 0]],
        [(700, 420), [14, 15, 17, 23]],
        [(70, 500), [1, 21]],
        [(70, 210), [1, 2, 4, 6, 7, 22]],
        [(450, 700), [5, 19, 0, 23]],
        [(45, 45), [0, 3, 20]],
        [(1225, 700), [18, 21]]
    ],
    [
        [(0, 0), [1, 4]],
        [(0, 100), [0, 2, 5]],
        [(0, 200), [1, 3, 6]],
        [(0, 300), [2, 7]],
        [(100, 0), [5, 0, 8]],
        [(100, 100), [4, 6, 1, 9]],
        [(100, 200), [5, 7, 2, 10]],
        [(100, 300), [6, 3, 11]],
        [(200, 0), [9, 4, 12]],
        [(200, 100), [8, 10, 5, 13]],
        [(200, 200), [9, 11, 6, 14]],
        [(200, 300), [10, 7, 15]],
        [(300, 0), [13, 8]],
        [(300, 100), [12, 14, 9]],
        [(300, 200), [13, 15, 10]],
        [(300, 300), [14,11]],
    ],
    [
        [(45, 45), [1]],
        [(100, 245), [0, 2, 4]],
        [(200, 245), [1, 3, 5]],
        [(300, 145), [2, 6]],
        [(100, 345), [1, 5, 7]],
        [(200, 345), [2, 4, 6, 8]],
        [(300, 345), [3, 9]],
        [(100, 545), [4, 8]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [6, 8, 10]],
        [(1200, 700), [9]]
    ],
    [
        [(45, 45), [1]],
        [(100, 245), [14, 0, 2]],
        [(200, 245), [1, 5, 3]],
        [(300, 245), [2, 6, 10, 11, 12]],
        [(500, 345), [13, 6, 9]],
        [(200, 345), [14, 2, 6, 8]],
        [(300, 345), [9, 5, 4, 3]],
        [(100, 545), [8, 14]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [4, 6, 8, 15]],
        [(200, 145), [3, 11]],
        [(300, 145), [3, 10, 12]],
        [(400, 145), [3, 11, 13]],
        [(500, 145), [4, 12]],
        [(100, 345), [1, 7, 5]],
        [(1200, 700), [9]],
    ],

    #new graph 1 
    [
        [(0, 0), [1]],          
        [(100, 50), [0, 2]],
        [(200, 50), [1, 3]],
        [(300, 100), [2, 4]],
        [(400, 100), [3, 5]],
        [(500, 150), [4, 6]],
        [(600, 200), [5, 7]],
        [(700, 250), [6, 8]],
        [(800, 300), [7, 9]],
        [(900, 350), [8]],        
    ],

    #new graph 2
    [
        [(0, 0), [1]],                  
        [(100, 20), [0, 2]],           
        [(200, 40), [1, 3]],           
        [(300, 60), [2, 4]],           
        [(400, 80), [3, 5]],           
        [(500, 100), [4, 6]],          
        [(600, 120), [5, 7]],          
        [(700, 140), [6, 8]],          
        [(800, 160), [7, 9]],          
        [(900, 180), [8]],              
    ],

    #new graph 3
    [
        [(0, 10), [1]],                  
        [(100, 20), [0, 2]],           
        [(200, 30), [1, 3]],           
        [(300, 40), [2, 4]],           
        [(400, 50), [3, 5]],           
        [(500, 60), [4, 6]],          
        [(600, 70), [5, 7]],          
        [(700, 80), [6, 8]],          
        [(800, 90), [7, 9]],          
        [(900, 100), [8]],              
    ],

    #extra credit graph
    [
        [(0, 0), [1, 5, 6]],
        [(100, 0), [0, 2, 7]],
        [(200, 0), [1, 3, 8]],
        [(300, 0), [2, 4]],
        [(400, 0), [3, 9]],
        [(0, 100), [0, 10]],
        [(100, 100), [0, 7, 11]],
        [(200, 100), [1, 6, 12]],
        [(300, 100), [2, 7, 9]],
        [(400, 100), [4, 8, 13]],
        [(0, 200), [5, 11, 15]],
        [(100, 200), [6, 10, 16]],
        [(200, 200), [7, 11, 17]],
        [(300, 200), [9, 12, 14]],
        [(400, 200), [13, 19]],
        [(0, 300), [10, 16, 20]],
        [(100, 300), [11, 15, 21]],
        [(200, 300), [12, 16, 18]],
        [(300, 300), [17, 19, 23]],
        [(400, 300), [14, 18, 24]],
        [(0, 400), [15, 21]],
        [(100, 400), [16, 20, 22]],
        [(200, 400), [21, 23]],
        [(300, 400), [18, 22, 24]],
        [(400, 400), [19, 23]]
],
  
  
]

test_path = [
    [1, 2],
    [1, 2, 3],
    [22, 3, 11, 17, 18, 23],
    [1, 5, 6, 10, 11, 15],
    [1, 2, 5, 8, 9, 10],
    [1, 14, 5, 6, 9, 15],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], #test path for new graph 1
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], #test path for new graph 2
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], #test path for new graph 3
    [0, 1, 2, 4, 6, 9, 11, 9, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24], #test path for extra credit graph
]