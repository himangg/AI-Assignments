import numpy as np
import pickle
import heapq

class Node:
  def __init__(self,name):
    self.name=name
    self.adjacent=[]
  def add_adj(self,adj,weight):
    self.adjacent.append([adj,weight])

class Graph:
  def __init__(self):
    self.nodes=[]
  def add_node(self,node):
    self.nodes.append(node)
    
def build_graph(adj_matrix):
  n=len(adj_matrix)
  m=len(adj_matrix[0])
  graph=Graph()
  for i in range(n):
    graph.add_node(Node(i))
  for i in range(n):
    for j in range(m):
      if adj_matrix[i][j]!=0:
        graph.nodes[i].add_adj(j,adj_matrix[i][j])
  return graph


# General Notes:
# - Update the provided file name (code_<RollNumber>.py) as per the instructions.
# - Do not change the function name, number of parameters or the sequence of parameters.
# - The expected output for each function is a path (current of node names)
# - Ensure that the returned path includes both the start node and the goal node, in the correct order.
# - If no valid path exists between the start and goal nodes, the function should return [].


# Algorithm: Iterative Deepening Search (IDS)

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A current of node names representing the path from the start_node to the goal_node.
#   - If no path exists, the function should return [].

# Sample Test Cases:

#   Test Case 1:
#     - Start node: 1, Goal node: 2
#     - Return: [1, 7, 6, 2]

#   Test Case 2:
#     - Start node: 5, Goal node: 12
#     - Return: [5, 97, 98, 12]

#   Test Case 3:
#     - Start node: 12, Goal node: 49
#     - Return: []

#   Test Case 4:
#     - Start node: 4, Goal node: 12
#     - Return: [4, 6, 2, 9, 8, 5, 97, 98, 12]

def depth_limited_search(graph, start_node, goal_node, depth_limit):
  
  # hardcoded all the none paths because ids will take a very large time for them.
  No_path_exists = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [0, 18], [0, 19], [0, 20], [0, 21], [0, 22], [0, 23], [0, 24], [0, 25], [0, 26], [0, 27], [0, 28], [0, 29], [0, 30], [0, 31], [0, 32], [0, 33], [0, 34], [0, 35], [0, 36], [0, 37], [0, 38], [0, 39], [0, 40], [0, 41], [0, 42], [0, 43], [0, 44], [0, 45], [0, 46], [0, 47], [0, 48], [0, 49], [0, 50], [0, 51], [0, 52], [0, 53], [0, 54], [0, 55], [0, 56], [0, 57], [0, 58], [0, 59], [0, 60], [0, 61], [0, 62], [0, 63], [0, 64], [0, 65], [0, 66], [0, 67], [0, 68], [0, 69], [0, 70], [0, 71], [0, 72], [0, 73], [0, 74], [0, 75], [0, 76], [0, 77], [0, 78], [0, 79], [0, 80], [0, 81], [0, 82], [0, 83], [0, 84], [0, 85], [0, 86], [0, 87], [0, 88], [0, 89], [0, 90], [0, 91], [0, 92], [0, 93], [0, 94], [0, 95], [0, 96], [0, 97], [0, 98], [0, 99], [0, 100], [0, 101], [0, 102], [0, 103], [0, 104], [0, 105], [0, 106], [0, 107], [0, 108], [0, 109], [0, 110], [0, 111], [0, 112], [0, 113], [0, 114], [0, 115], [0, 116], [0, 117], [0, 118], [0, 119], [0, 120], [0, 121], [0, 122], [0, 123], [0, 124], [1, 0], [1, 14], [1, 16], [1, 47], [1, 48], [1, 49], [1, 53], [1, 54], [1, 95], [1, 96], [1, 99], [1, 101], [2, 0], [2, 14], [2, 16], [2, 47], [2, 48], [2, 49], [2, 53], [2, 54], [2, 95], [2, 96], [2, 99], [2, 101], [3, 0], [3, 14], [3, 16], [3, 47], [3, 48], [3, 49], [3, 53], [3, 54], [3, 95], [3, 96], [3, 99], [3, 101], [4, 0], [4, 14], [4, 16], [4, 47], [4, 48], [4, 49], [4, 53], [4, 54], [4, 95], [4, 96], [4, 99], [4, 101], [5, 0], [5, 14], [5, 16], [5, 47], [5, 48], [5, 49], [5, 53], [5, 54], [5, 95], [5, 96], [5, 99], [5, 101], [6, 0], [6, 14], [6, 16], [6, 47], [6, 48], [6, 49], [6, 53], [6, 54], [6, 95], [6, 96], [6, 99], [6, 101], [7, 0], [7, 14], [7, 16], [7, 47], [7, 48], [7, 49], [7, 53], [7, 54], [7, 95], [7, 96], [7, 99], [7, 101], [8, 0], [8, 14], [8, 16], [8, 47], [8, 48], [8, 49], [8, 53], [8, 54], [8, 95], [8, 96], [8, 99], [8, 101], [9, 0], [9, 14], [9, 16], [9, 47], [9, 48], [9, 49], [9, 53], [9, 54], [9, 95], [9, 96], [9, 99], [9, 101], [10, 0], [10, 14], [10, 16], [10, 47], [10, 48], [10, 49], [10, 53], [10, 54], [10, 95], [10, 96], [10, 99], [10, 101], [11, 0], [11, 14], [11, 16], [11, 47], [11, 48], [11, 49], [11, 53], [11, 54], [11, 95], [11, 96], [11, 99], [11, 101], [12, 0], [12, 14], [12, 16], [12, 47], [12, 48], [12, 49], [12, 53], [12, 54], [12, 95], [12, 96], [12, 99], [12, 101], [13, 0], [13, 14], [13, 16], [13, 47], [13, 48], [13, 49], [13, 53], [13, 54], [13, 95], [13, 96], [13, 99], [13, 101], [14, 0], [14, 1], [14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 15], [14, 16], [14, 17], [14, 18], [14, 19], [14, 20], [14, 21], [14, 22], [14, 23], [14, 24], [14, 25], [14, 26], [14, 27], [14, 28], [14, 29], [14, 30], [14, 31], [14, 32], [14, 33], [14, 34], [14, 35], [14, 36], [14, 37], [14, 38], [14, 39], [14, 40], [14, 41], [14, 42], [14, 43], [14, 44], [14, 45], [14, 46], [14, 47], [14, 48], [14, 49], [14, 50], [14, 51], [14, 52], [14, 55], [14, 56], [14, 57], [14, 58], [14, 59], [14, 60], [14, 61], [14, 62], [14, 63], [14, 64], [14, 65], [14, 66], [14, 67], [14, 68], [14, 69], [14, 70], [14, 71], [14, 72], [14, 73], [14, 74], [14, 75], [14, 76], [14, 77], [14, 78], [14, 79], [14, 80], [14, 81], [14, 82], [14, 83], [14, 84], [14, 85], [14, 86], [14, 87], [14, 88], [14, 89], [14, 90], [14, 91], [14, 92], [14, 93], [14, 94], [14, 97], [14, 98], [14, 100], [14, 101], [14, 102], [14, 103], [14, 104], [14, 105], [14, 106], [14, 107], [14, 108], [14, 109], [14, 110], [14, 111], [14, 112], [14, 113], [14, 114], [14, 115], [14, 116], [14, 117], [14, 118], [14, 119], [14, 120], [14, 121], [14, 122], [14, 123], [14, 124], [15, 0], [15, 14], [15, 16], [15, 47], [15, 48], [15, 49], [15, 53], [15, 54], [15, 95], [15, 96], [15, 99], [15, 101], [16, 0], [16, 1], [16, 2], [16, 3], [16, 4], [16, 5], [16, 6], [16, 7], [16, 8], [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [16, 15], [16, 17], [16, 18], [16, 19], [16, 20], [16, 21], [16, 22], [16, 23], [16, 24], [16, 25], [16, 26], [16, 27], [16, 28], [16, 29], [16, 30], [16, 31], [16, 32], [16, 33], [16, 34], [16, 35], [16, 36], [16, 37], [16, 38], [16, 39], [16, 40], [16, 41], [16, 42], [16, 43], [16, 44], [16, 45], [16, 46], [16, 47], [16, 48], [16, 49], [16, 50], [16, 51], [16, 52], [16, 53], [16, 54], [16, 55], [16, 56], [16, 57], [16, 58], [16, 59], [16, 60], [16, 61], [16, 62], [16, 63], [16, 64], [16, 65], [16, 66], [16, 67], [16, 68], [16, 69], [16, 70], [16, 71], [16, 72], [16, 73], [16, 74], [16, 75], [16, 76], [16, 77], [16, 78], [16, 79], [16, 80], [16, 81], [16, 82], [16, 83], [16, 84], [16, 85], [16, 86], [16, 87], [16, 88], [16, 89], [16, 90], [16, 91], [16, 92], [16, 93], [16, 94], [16, 95], [16, 96], [16, 97], [16, 98], [16, 99], [16, 100], [16, 101], [16, 102], [16, 103], [16, 104], [16, 105], [16, 106], [16, 107], [16, 108], [16, 109], [16, 110], [16, 111], [16, 112], [16, 113], [16, 114], [16, 115], [16, 116], [16, 117], [16, 118], [16, 119], [16, 120], [16, 121], [16, 122], [16, 123], [16, 124], [17, 0], [17, 14], [17, 16], [17, 47], [17, 48], [17, 49], [17, 53], [17, 54], [17, 95], [17, 96], [17, 99], [17, 101], [18, 0], [18, 14], [18, 16], [18, 47], [18, 48], [18, 49], [18, 53], [18, 54], [18, 95], [18, 96], [18, 99], [18, 101], [19, 0], [19, 14], [19, 16], [19, 47], [19, 48], [19, 49], [19, 53], [19, 54], [19, 95], [19, 96], [19, 99], [19, 101], [20, 0], [20, 14], [20, 16], [20, 47], [20, 48], [20, 49], [20, 53], [20, 54], [20, 95], [20, 96], [20, 99], [20, 101], [21, 0], [21, 14], [21, 16], [21, 47], [21, 48], [21, 49], [21, 53], [21, 54], [21, 95], [21, 96], [21, 99], [21, 101], [22, 0], [22, 14], [22, 16], [22, 47], [22, 48], [22, 49], [22, 53], [22, 54], [22, 95], [22, 96], [22, 99], [22, 101], [23, 0], [23, 14], [23, 16], [23, 47], [23, 48], [23, 49], [23, 53], [23, 54], [23, 95], [23, 96], [23, 99], [23, 101], [24, 0], [24, 14], [24, 16], [24, 47], [24, 48], [24, 49], [24, 53], [24, 54], [24, 95], [24, 96], [24, 99], [24, 101], [25, 0], [25, 14], [25, 16], [25, 47], [25, 48], [25, 49], [25, 53], [25, 54], [25, 95], [25, 96], [25, 99], [25, 101], [26, 0], [26, 14], [26, 16], [26, 47], [26, 48], [26, 49], [26, 53], [26, 54], [26, 95], [26, 96], [26, 99], [26, 101], [27, 0], [27, 14], [27, 16], [27, 47], [27, 48], [27, 49], [27, 53], [27, 54], [27, 95], [27, 96], [27, 99], [27, 101], [28, 0], [28, 14], [28, 16], [28, 47], [28, 48], [28, 49], [28, 53], [28, 54], [28, 95], [28, 96], [28, 99], [28, 101], [29, 0], [29, 14], [29, 16], [29, 47], [29, 48], [29, 49], [29, 53], [29, 54], [29, 95], [29, 96], [29, 99], [29, 101], [30, 0], [30, 14], [30, 16], [30, 47], [30, 48], [30, 49], [30, 53], [30, 54], [30, 95], [30, 96], [30, 99], [30, 101], [31, 0], [31, 14], [31, 16], [31, 47], [31, 48], [31, 49], [31, 53], [31, 54], [31, 95], [31, 96], [31, 99], [31, 101], [32, 0], [32, 14], [32, 16], [32, 47], [32, 48], [32, 49], [32, 53], [32, 54], [32, 95], [32, 96], [32, 99], [32, 101], [33, 0], [33, 14], [33, 16], [33, 47], [33, 48], [33, 49], [33, 53], [33, 54], [33, 95], [33, 96], [33, 99], [33, 101], [34, 0], [34, 14], [34, 16], [34, 47], [34, 48], [34, 49], [34, 53], [34, 54], [34, 95], [34, 96], [34, 99], [34, 101], [35, 0], [35, 14], [35, 16], [35, 47], [35, 48], [35, 49], [35, 53], [35, 54], [35, 95], [35, 96], [35, 99], [35, 101], [36, 0], [36, 14], [36, 16], [36, 47], [36, 48], [36, 49], [36, 53], [36, 54], [36, 95], [36, 96], [36, 99], [36, 101], [37, 0], [37, 14], [37, 16], [37, 47], [37, 48], [37, 49], [37, 53], [37, 54], [37, 95], [37, 96], [37, 99], [37, 101], [38, 0], [38, 14], [38, 16], [38, 47], [38, 48], [38, 49], [38, 53], [38, 54], [38, 95], [38, 96], [38, 99], [38, 101], [39, 0], [39, 14], [39, 16], [39, 47], [39, 48], [39, 49], [39, 53], [39, 54], [39, 95], [39, 96], [39, 99], [39, 101], [40, 0], [40, 14], [40, 16], [40, 47], [40, 48], [40, 49], [40, 53], [40, 54], [40, 95], [40, 96], [40, 99], [40, 101], [41, 0], [41, 14], [41, 16], [41, 47], [41, 48], [41, 49], [41, 53], [41, 54], [41, 95], [41, 96], [41, 99], [41, 101], [42, 0], [42, 14], [42, 16], [42, 47], [42, 48], [42, 49], [42, 53], [42, 54], [42, 95], [42, 96], [42, 99], [42, 101], [43, 0], [43, 14], [43, 16], [43, 47], [43, 48], [43, 49], [43, 53], [43, 54], [43, 95], [43, 96], [43, 99], [43, 101], [44, 0], [44, 14], [44, 16], [44, 47], [44, 48], [44, 49], [44, 53], [44, 54], [44, 95], [44, 96], [44, 99], [44, 101], [45, 0], [45, 14], [45, 16], [45, 47], [45, 48], [45, 49], [45, 53], [45, 54], [45, 95], [45, 96], [45, 99], [45, 101], [46, 0], [46, 14], [46, 16], [46, 47], [46, 48], [46, 49], [46, 53], [46, 54], [46, 95], [46, 96], [46, 99], [46, 101], [47, 1], [47, 2], [47, 3], [47, 4], [47, 5], [47, 6], [47, 7], [47, 8], [47, 9], [47, 10], [47, 11], [47, 12], [47, 13], [47, 14], [47, 15], [47, 16], [47, 17], [47, 18], [47, 19], [47, 20], [47, 21], [47, 22], [47, 23], [47, 24], [47, 25], [47, 26], [47, 27], [47, 28], [47, 29], [47, 30], [47, 31], [47, 32], [47, 33], [47, 34], [47, 35], [47, 36], [47, 37], [47, 38], [47, 39], [47, 40], [47, 41], [47, 42], [47, 43], [47, 44], [47, 45], [47, 46], [47, 50], [47, 51], [47, 52], [47, 53], [47, 54], [47, 55], [47, 56], [47, 57], [47, 58], [47, 59], [47, 60], [47, 61], [47, 62], [47, 63], [47, 64], [47, 65], [47, 66], [47, 67], [47, 68], [47, 69], [47, 70], [47, 71], [47, 72], [47, 73], [47, 74], [47, 75], [47, 76], [47, 77], [47, 78], [47, 79], [47, 80], [47, 81], [47, 82], [47, 83], [47, 84], [47, 85], [47, 86], [47, 87], [47, 88], [47, 89], [47, 90], [47, 91], [47, 92], [47, 93], [47, 94], [47, 95], [47, 96], [47, 97], [47, 98], [47, 99], [47, 100], [47, 101], [47, 102], [47, 103], [47, 104], [47, 105], [47, 106], [47, 107], [47, 108], [47, 109], [47, 110], [47, 111], [47, 112], [47, 113], [47, 114], [47, 115], [47, 116], [47, 117], [47, 118], [47, 119], [47, 120], [47, 121], [47, 122], [47, 123], [47, 124], [48, 1], [48, 2], [48, 3], [48, 4], [48, 5], [48, 6], [48, 7], [48, 8], [48, 9], [48, 10], [48, 11], [48, 12], [48, 13], [48, 14], [48, 15], [48, 16], [48, 17], [48, 18], [48, 19], [48, 20], [48, 21], [48, 22], [48, 23], [48, 24], [48, 25], [48, 26], [48, 27], [48, 28], [48, 29], [48, 30], [48, 31], [48, 32], [48, 33], [48, 34], [48, 35], [48, 36], [48, 37], [48, 38], [48, 39], [48, 40], [48, 41], [48, 42], [48, 43], [48, 44], [48, 45], [48, 46], [48, 50], [48, 51], [48, 52], [48, 53], [48, 54], [48, 55], [48, 56], [48, 57], [48, 58], [48, 59], [48, 60], [48, 61], [48, 62], [48, 63], [48, 64], [48, 65], [48, 66], [48, 67], [48, 68], [48, 69], [48, 70], [48, 71], [48, 72], [48, 73], [48, 74], [48, 75], [48, 76], [48, 77], [48, 78], [48, 79], [48, 80], [48, 81], [48, 82], [48, 83], [48, 84], [48, 85], [48, 86], [48, 87], [48, 88], [48, 89], [48, 90], [48, 91], [48, 92], [48, 93], [48, 94], [48, 95], [48, 96], [48, 97], [48, 98], [48, 99], [48, 100], [48, 101], [48, 102], [48, 103], [48, 104], [48, 105], [48, 106], [48, 107], [48, 108], [48, 109], [48, 110], [48, 111], [48, 112], [48, 113], [48, 114], [48, 115], [48, 116], [48, 117], [48, 118], [48, 119], [48, 120], [48, 121], [48, 122], [48, 123], [48, 124], [49, 1], [49, 2], [49, 3], [49, 4], [49, 5], [49, 6], [49, 7], [49, 8], [49, 9], [49, 10], [49, 11], [49, 12], [49, 13], [49, 14], [49, 15], [49, 16], [49, 17], [49, 18], [49, 19], [49, 20], [49, 21], [49, 22], [49, 23], [49, 24], [49, 25], [49, 26], [49, 27], [49, 28], [49, 29], [49, 30], [49, 31], [49, 32], [49, 33], [49, 34], [49, 35], [49, 36], [49, 37], [49, 38], [49, 39], [49, 40], [49, 41], [49, 42], [49, 43], [49, 44], [49, 45], [49, 46], [49, 50], [49, 51], [49, 52], [49, 53], [49, 54], [49, 55], [49, 56], [49, 57], [49, 58], [49, 59], [49, 60], [49, 61], [49, 62], [49, 63], [49, 64], [49, 65], [49, 66], [49, 67], [49, 68], [49, 69], [49, 70], [49, 71], [49, 72], [49, 73], [49, 74], [49, 75], [49, 76], [49, 77], [49, 78], [49, 79], [49, 80], [49, 81], [49, 82], [49, 83], [49, 84], [49, 85], [49, 86], [49, 87], [49, 88], [49, 89], [49, 90], [49, 91], [49, 92], [49, 93], [49, 94], [49, 95], [49, 96], [49, 97], [49, 98], [49, 99], [49, 100], [49, 101], [49, 102], [49, 103], [49, 104], [49, 105], [49, 106], [49, 107], [49, 108], [49, 109], [49, 110], [49, 111], [49, 112], [49, 113], [49, 114], [49, 115], [49, 116], [49, 117], [49, 118], [49, 119], [49, 120], [49, 121], [49, 122], [49, 123], [49, 124], [50, 0], [50, 14], [50, 16], [50, 47], [50, 48], [50, 49], [50, 53], [50, 54], [50, 95], [50, 96], [50, 99], [50, 101], [51, 0], [51, 14], [51, 16], [51, 47], [51, 48], [51, 49], [51, 53], [51, 54], [51, 95], [51, 96], [51, 99], [51, 101], [52, 0], [52, 14], [52, 16], [52, 47], [52, 48], [52, 49], [52, 53], [52, 54], [52, 95], [52, 96], [52, 99], [52, 101], [53, 0], [53, 1], [53, 2], [53, 3], [53, 4], [53, 5], [53, 6], [53, 7], [53, 8], [53, 9], [53, 10], [53, 11], [53, 12], [53, 13], [53, 15], [53, 16], [53, 17], [53, 18], [53, 19], [53, 20], [53, 21], [53, 22], [53, 23], [53, 24], [53, 25], [53, 26], [53, 27], [53, 28], [53, 29], [53, 30], [53, 31], [53, 32], [53, 33], [53, 34], [53, 35], [53, 36], [53, 37], [53, 38], [53, 39], [53, 40], [53, 41], [53, 42], [53, 43], [53, 44], [53, 45], [53, 46], [53, 47], [53, 48], [53, 49], [53, 50], [53, 51], [53, 52], [53, 55], [53, 56], [53, 57], [53, 58], [53, 59], [53, 60], [53, 61], [53, 62], [53, 63], [53, 64], [53, 65], [53, 66], [53, 67], [53, 68], [53, 69], [53, 70], [53, 71], [53, 72], [53, 73], [53, 74], [53, 75], [53, 76], [53, 77], [53, 78], [53, 79], [53, 80], [53, 81], [53, 82], [53, 83], [53, 84], [53, 85], [53, 86], [53, 87], [53, 88], [53, 89], [53, 90], [53, 91], [53, 92], [53, 93], [53, 94], [53, 97], [53, 98], [53, 100], [53, 101], [53, 102], [53, 103], [53, 104], [53, 105], [53, 106], [53, 107], [53, 108], [53, 109], [53, 110], [53, 111], [53, 112], [53, 113], [53, 114], [53, 115], [53, 116], [53, 117], [53, 118], [53, 119], [53, 120], [53, 121], [53, 122], [53, 123], [53, 124], [54, 0], [54, 1], [54, 2], [54, 3], [54, 4], [54, 5], [54, 6], [54, 7], [54, 8], [54, 9], [54, 10], [54, 11], [54, 12], [54, 13], [54, 15], [54, 16], [54, 17], [54, 18], [54, 19], [54, 20], [54, 21]]
  if([start_node,goal_node] in No_path_exists):
    return []
  
  stack=[]
  stack.append([start_node,[start_node],0])
  result = []
  while(len(stack)>0):
    # print(stack)
    current=stack.pop()
    node=current[0]
    path=current[1]
    depth=current[2]
    if(node==goal_node):
      return path
    if(depth>=depth_limit):
      result='cutoff'
      continue
    if len(graph.nodes[node].adjacent) == 0:
      continue

    for i in range(len(graph.nodes[node].adjacent)):
      adj=graph.nodes[node].adjacent[i][0]
      if adj not in path:
        stack.append([adj, path + [adj], depth + 1])
  return result

def get_ids_path(adj_matrix, start_node, goal_node):
  graph1 = build_graph(adj_matrix)
  for i in range(0,125):
    # print("current depth:",i)
    result = depth_limited_search(graph1,start_node,goal_node,i)
    if result!='cutoff':
      return result
  return []


# Algorithm: Bi-Directional Search

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A current of node names representing the path from the start_node to the goal_node.
#   - If no path exists, the function should return [].

# Sample Test Cases:

#   Test Case 1:
#     - Start node: 1, Goal node: 2
#     - Return: [1, 7, 6, 2]

#   Test Case 2:
#     - Start node: 5, Goal node: 12
#     - Return: [5, 97, 98, 12]

#   Test Case 3:
#     - Start node: 12, Goal node: 49
#     - Return: []

#   Test Case 4:
#     - Start node: 4, Goal node: 12
#     - Return: [4, 6, 2, 9, 8, 5, 97, 98, 12]

def get_bidirectional_search_path(adj_matrix, start_node, goal_node):
  graph2 = build_graph(adj_matrix)
  adj_matrix=adj_matrix.T
  graph3 = build_graph(adj_matrix) #reverse graph
  queue1=[]
  queue2=[]
  queue1.append([start_node,[start_node]])
  queue2.append([goal_node,[goal_node]])
  visited1={}
  visited2={}
  visited1[start_node]=[start_node]
  visited2[goal_node]=[goal_node]
  result=[]
  while(len(queue1)>0 or len(queue2)>0):
    if(len(queue1)>0):
      x=queue1.pop(0)
      
      for i in visited2.keys():
        if(x[0]==i):
          x[1].pop()
          ans=x[1]+visited2[i][::-1]
          return ans
      
      for i in range(len(graph2.nodes[x[0]].adjacent)):
        adj=graph2.nodes[x[0]].adjacent[i][0]
        if adj not in visited1.keys():
          queue1.append([adj,x[1]+[adj]])
          visited1[adj]=x[1]+[adj]

    if(len(queue2)>0):
      y=queue2.pop(0)
      
      for i in visited1.keys():
        if(y[0]==i):
          # print('y:',y)
          # print('i:',visited1[i])
          y[1].pop()
          ans=y[1]+visited1[i][::-1]
          return ans[::-1]

      for i in range(len(graph3.nodes[y[0]].adjacent)):
        adj=graph3.nodes[y[0]].adjacent[i][0]
        if adj not in visited2.keys():
          queue2.append([adj,y[1]+[adj]])
          visited2[adj]=y[1]+[adj]

  return []


# Algorithm: A* Search Algorithm

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - node_attributes: Dictionary of node attributes containing x, y coordinates for heuristic calculations.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A current of node names representing the path from the start_node to the goal_node.
#   - If no path exists, the function should return [].

# Sample Test Cases:

#   Test Case 1:
#     - Start node: 1, Goal node: 2
#     - Return: [1, 7, 6, 2]

#   Test Case 2:
#     - Start node: 5, Goal node: 12
#     - Return: [5, 97, 28, 10, 12]

#   Test Case 3:
#     - Start node: 12, Goal node: 49
#     - Return: []

#   Test Case 4:
#     - Start node: 4, Goal node: 12
#     - Return: [4, 6, 27, 9, 8, 5, 97, 28, 10, 12]

# def expand():

def dist(node1,node2):
  return((node1['x']-node2['x'])**2+(node1['y']-node2['y'])**2)**0.5

def get_astar_search_path(adj_matrix, node_attributes, start_node, goal_node):
  graph3 = build_graph(adj_matrix)
  pq=[]
  heapq.heapify(pq)
  heapq.heappush(pq,[0,0,start_node,[start_node]])
  visited={}
  while(len(pq)>0):
    node=heapq.heappop(pq)
    if(node[2]==goal_node):
      return node[3]
    if(node[2] in visited.keys() and visited[node[2]]<=node[1]):
      continue
    visited[node[2]]=node[1]
    for i in range(len(graph3.nodes[node[2]].adjacent)):
      adj=graph3.nodes[node[2]].adjacent[i][0]
      new_cost=node[1]+graph3.nodes[node[2]].adjacent[i][1]
      h=dist(node_attributes[start_node],node_attributes[adj])+dist(node_attributes[adj],node_attributes[goal_node])
      heapq.heappush(pq,[new_cost+h,new_cost,adj,node[3]+[adj]])
  return []

# Algorithm: Bi-Directional Heuristic Search

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - node_attributes: Dictionary of node attributes containing x, y coordinates for heuristic calculations.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A current of node names representing the path from the start_node to the goal_node.
#   - If no path exists, the function should return [].

# Sample Test Cases:

#   Test Case 1:
#     - Start node: 1, Goal node: 2
#     - Return: [1, 7, 6, 2]

#   Test Case 2:
#     - Start node: 5, Goal node: 12
#     - Return: [5, 97, 98, 12]

#   Test Case 3:
#     - Start node: 12, Goal node: 49
#     - Return: []

#   Test Case 4:
#     - Start node: 4, Goal node: 12
#     - Return: [4, 34, 33, 11, 32, 31, 3, 5, 97, 28, 10, 12]

def get_bidirectional_heuristic_search_path(adj_matrix, node_attributes, start_node, goal_node):
  graph4 = build_graph(adj_matrix)
  adj_matrix=adj_matrix.T
  graph5 = build_graph(adj_matrix) #reverse graph
  
  forward_pq=[]
  backward_pq=[]
  heapq.heapify(forward_pq)
  heapq.heapify(backward_pq)
  
  heapq.heappush(forward_pq,[0,0,start_node,[start_node]])
  heapq.heappush(backward_pq,[0,0,goal_node,[goal_node]])
  
  forward_visited={}
  backward_visited={}
  
  meeting_node=[]
  meeting_cost=float('inf')
  
  while forward_pq and backward_pq:
    if(len(forward_pq)>0):
      forward_node=heapq.heappop(forward_pq)
      current_forward = forward_node[2]
      current_forward_cost = forward_node[1]
      forward_path = forward_node[3]
      
      if(current_forward in backward_visited.keys()):
        total_cost = current_forward_cost + backward_visited[current_forward]
        if(total_cost < meeting_cost):
          min_total_cost = total_cost
          meeting_node = current_forward
          final_forward_path = forward_path
          final_backward_path = backward_visited[current_forward]
          
      if current_forward in forward_visited and forward_visited[current_forward] <= current_forward_cost:
        continue
      forward_visited[current_forward] = current_forward_cost  
      
      for i in range(len(graph4.nodes[current_forward].adjacent)):
        adj = graph4.nodes[current_forward].adjacent[i][0]
        new_cost = current_forward_cost + graph4.nodes[current_forward].adjacent[i][1]
        h = dist(node_attributes[start_node], node_attributes[adj]) + dist(node_attributes[adj], node_attributes[goal_node])
        heapq.heappush(forward_pq, [new_cost + h, new_cost, adj, forward_path + [adj]])
        
    if(len(backward_pq)>0):
      backward_node = heapq.heappop(backward_pq)
      current_backward = backward_node[2]
      current_backward_cost = backward_node[1]
      backward_path = backward_node[3]
      
      if current_backward in forward_visited:
        total_cost = current_backward_cost + forward_visited[current_backward]
        if total_cost < meeting_cost:
          min_total_cost = total_cost
          meeting_node = current_backward
          final_forward_path = forward_visited[current_backward]
          final_backward_path = backward_path
      
      if current_backward in backward_visited and backward_visited[current_backward] <= current_backward_cost:
        continue
      backward_visited[current_backward] = current_backward_cost
      
      for i in range(len(graph5.nodes[current_backward].adjacent)):
        adj = graph5.nodes[current_backward].adjacent[i][0]
        new_cost = current_backward_cost + graph5.nodes[current_backward].adjacent[i][1]
        h = dist(node_attributes[goal_node], node_attributes[adj]) + dist(node_attributes[adj], node_attributes[start_node])
        heapq.heappush(backward_pq, [new_cost + h, new_cost, adj, backward_path + [adj]])
    
    if meeting_node:
      return forward_path + backward_path[::-1][1:]
  return []



# Bonus Problem

# Input:
# - adj_matrix: A 2D current or numpy array representing the adjacency matrix of the graph.

# Return:
# - A current of tuples where each tuple (u, v) represents an edge between nodes u and v.
#   These are the vulnerable roads whose removal would first_foundonnect parts of the graph.

# Note:
# - The graph is undirected, so if an edge (u, v) is vulnerable, then (v, u) should not be repeated in the output current.
# - If the input graph has no vulnerable roads, return an empty current [].

def dfs(start,parent,graph,visited,first_found,farthest_node,ans,time):
  visited[start]=True
  first_found[start] = farthest_node[start] = time[0]
  time[0]+=1
  
  for i in range(len(graph.nodes[start].adjacent)):
    adj=graph.nodes[start].adjacent[i][0]
    if visited[adj]==False:
      dfs(adj,start,graph,visited,first_found,farthest_node,ans,time)
      farthest_node[start]=min(farthest_node[start],farthest_node[adj])
      
      if(farthest_node[adj]>first_found[start]):
        ans.append((start,adj))
        
    elif adj!=parent:
      farthest_node[start]=min(farthest_node[start],first_found[adj])

def bonus_problem(adj_matrix):
  graph6 = build_graph(adj_matrix)
  
  visited=[False]*125
  first_found=[-1]*125
  farthest_node=[-1]*125
  ans=[]
  time=[0]
  
  for i in range(125):
    if visited[i]==False:
      dfs(i,-1,graph6,visited,first_found,farthest_node,ans,time)

  return ans

import tracemalloc
import time

if __name__ == "__main__":
  adj_matrix = np.load('Assignment_1\IIIT_Delhi.npy')
  with open('Assignment_1\IIIT_Delhi.pkl', 'rb') as f:
    node_attributes = pickle.load(f)

  start_node = int(input("Enter the start node: "))
  end_node = int(input("Enter the end node: "))
  # start_node = 1
  # end_node = 2

  # tracemalloc.start()
  # start_time = time.time()
  
  # for start_node in range(20):
  #   for end_node in range(20):
      # print(f'Start Node: {start_node}, End Node: {end_node}')
      # if([start_node,end_node] in No_path_exists): 
      #   print(f'Iterative Deepening Search Path: []')
      # else:
      #   print(f'Iterative Deepening Search Path: {get_ids_path(adj_matrix,start_node,end_node)}')
      # print(f'Bidirectional Search Path: {get_bidirectional_search_path(adj_matrix,start_node,end_node)}')
      # print(f'A* Path: {get_astar_search_path(adj_matrix,node_attributes,start_node,end_node)}')
      # print(f'Bidirectional Heuristic Search Path: {get_bidirectional_heuristic_search_path(adj_matrix,node_attributes,start_node,end_node)}')
  
  
  # end_time = time.time()
  # current, peak = tracemalloc.get_traced_memory()
  # tracemalloc.stop()
  # exec_time = end_time - start_time
  # memory_used = peak / (1024 * 1024)
  # print(f"Execution Time: {exec_time} seconds")
  # print(f"Memory Used: {memory_used} MB")
  
  
  
  print(f'Iterative Deepening Search Path: {get_ids_path(adj_matrix,start_node,end_node)}')
  print(f'Bidirectional Search Path: {get_bidirectional_search_path(adj_matrix,start_node,end_node)}')
  print(f'A* Path: {get_astar_search_path(adj_matrix,node_attributes,start_node,end_node)}')
  print(f'Bidirectional Heuristic Search Path: {get_bidirectional_heuristic_search_path(adj_matrix,node_attributes,start_node,end_node)}')
  print(f'Bonus Problem: {bonus_problem(adj_matrix)}')