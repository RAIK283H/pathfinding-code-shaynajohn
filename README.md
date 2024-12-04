# Pathfinding Starter Code

random path algorithm:
the second requirement is that the player is not allowed to return to the starting node again.

The algorithm executes until the current node is the exit node.
It then checks if the target node is in the list of neighbors of the current node. If so, and the target node has not been visited yet, the next node visited is the target node.
If not, and it cannot return back to the starting node but it is in the list of neighbors, the starting node is then removed from the list. The next node then becomes a random picking from the list of neighbors.
If not, and the target node still hasn't been visited, the next node is the target node.
If not, the next node then becomes a random picking from the list of neighbors.
The path list adds on whatever the next node is.

statistic added:
the statistic added on was measuring how many seconds each players was going through the paths for


HW 7 Extra Credit:
*implemented in f_w.py as the very last function*
Sets edge weights to 1
Considers all possible intermediate pairs of nodes from i to k and k to j with the three nested for loops
Constructs path to target and adds path to exit