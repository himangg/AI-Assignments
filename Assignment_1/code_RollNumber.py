import numpy as np
import pickle


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
# - The expected output for each function is a path (list of node names)
# - Ensure that the returned path includes both the start node and the goal node, in the correct order.
# - If no valid path exists between the start and goal nodes, the function should return None.


# Algorithm: Iterative Deepening Search (IDS)

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A list of node names representing the path from the start_node to the goal_node.
#   - If no path exists, the function should return None.

# Sample Test Cases:

#   Test Case 1:
#     - Start node: 1, Goal node: 2
#     - Return: [1, 7, 6, 2]

#   Test Case 2:
#     - Start node: 5, Goal node: 12
#     - Return: [5, 97, 98, 12]

#   Test Case 3:
#     - Start node: 12, Goal node: 49
#     - Return: None

#   Test Case 4:
#     - Start node: 4, Goal node: 12
#     - Return: [4, 6, 2, 9, 8, 5, 97, 98, 12]

def depth_limited_search(graph, start_node, goal_node, depth_limit):
  stack=[]
  stack.append([start_node,[start_node],0])
  result = None
  visited=[]        #made a visited array to optimize the code
  while(len(stack)>0):
    # print(stack)
    list=stack.pop()
    node=list[0]
    path=list[1]
    depth=list[2]
    if(node in visited):
      continue
    else:
      visited.append(node)
      if(node==goal_node):
        return path
      if(depth>depth_limit):
        result='cutoff'
        continue

      for n,__,_ in stack:   #check cycle
          if(n==node):
              continue

      for i in range(len(graph.nodes[node].adjacent)):
        adj=graph.nodes[node].adjacent[i][0]
        stack.append([adj,path+[adj],depth+1])
      
  return result
  
def get_ids_path(adj_matrix, start_node, goal_node):
  graph1 = build_graph(adj_matrix)
  for i in range(0,126):
    print("current depth:",i)
    result = depth_limited_search(graph1,start_node,goal_node,i)
    if result!='cutoff':
      return result
  return None


# Algorithm: Bi-Directional Search

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A list of node names representing the path from the start_node to the goal_node.
#   - If no path exists, the function should return None.

# Sample Test Cases:

#   Test Case 1:
#     - Start node: 1, Goal node: 2
#     - Return: [1, 7, 6, 2]

#   Test Case 2:
#     - Start node: 5, Goal node: 12
#     - Return: [5, 97, 98, 12]

#   Test Case 3:
#     - Start node: 12, Goal node: 49
#     - Return: None

#   Test Case 4:
#     - Start node: 4, Goal node: 12
#     - Return: [4, 6, 2, 9, 8, 5, 97, 98, 12]

def get_bidirectional_search_path(adj_matrix, start_node, goal_node):

  return []


# Algorithm: A* Search Algorithm

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - node_attributes: Dictionary of node attributes containing x, y coordinates for heuristic calculations.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A list of node names representing the path from the start_node to the goal_node.
#   - If no path exists, the function should return None.

# Sample Test Cases:

#   Test Case 1:
#     - Start node: 1, Goal node: 2
#     - Return: [1, 7, 6, 2]

#   Test Case 2:
#     - Start node: 5, Goal node: 12
#     - Return: [5, 97, 28, 10, 12]

#   Test Case 3:
#     - Start node: 12, Goal node: 49
#     - Return: None

#   Test Case 4:
#     - Start node: 4, Goal node: 12
#     - Return: [4, 6, 27, 9, 8, 5, 97, 28, 10, 12]

def get_astar_search_path(adj_matrix, node_attributes, start_node, goal_node):

  return []


# Algorithm: Bi-Directional Heuristic Search

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - node_attributes: Dictionary of node attributes containing x, y coordinates for heuristic calculations.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A list of node names representing the path from the start_node to the goal_node.
#   - If no path exists, the function should return None.

# Sample Test Cases:

#   Test Case 1:
#     - Start node: 1, Goal node: 2
#     - Return: [1, 7, 6, 2]

#   Test Case 2:
#     - Start node: 5, Goal node: 12
#     - Return: [5, 97, 98, 12]

#   Test Case 3:
#     - Start node: 12, Goal node: 49
#     - Return: None

#   Test Case 4:
#     - Start node: 4, Goal node: 12
#     - Return: [4, 34, 33, 11, 32, 31, 3, 5, 97, 28, 10, 12]

def get_bidirectional_heuristic_search_path(adj_matrix, node_attributes, start_node, goal_node):

  return []



# Bonus Problem
 
# Input:
# - adj_matrix: A 2D list or numpy array representing the adjacency matrix of the graph.

# Return:
# - A list of tuples where each tuple (u, v) represents an edge between nodes u and v.
#   These are the vulnerable roads whose removal would disconnect parts of the graph.

# Note:
# - The graph is undirected, so if an edge (u, v) is vulnerable, then (v, u) should not be repeated in the output list.
# - If the input graph has no vulnerable roads, return an empty list [].

def bonus_problem(adj_matrix):

  return []


if __name__ == "__main__":
  adj_matrix = np.load('Assignment_1\IIIT_Delhi.npy')
  with open('Assignment_1\IIIT_Delhi.pkl', 'rb') as f:
    node_attributes = pickle.load(f)

  # print(sum(adj_matrix[1]))
  start_node = int(input("Enter the start node: "))
  end_node = int(input("Enter the end node: "))
  # start_node = 1
  # end_node = 2

  print(f'Iterative Deepening Search Path: {get_ids_path(adj_matrix,start_node,end_node)}')
  # print(f'Bidirectional Search Path: {get_bidirectional_search_path(adj_matrix,start_node,end_node)}')
  # print(f'A* Path: {get_astar_search_path(adj_matrix,node_attributes,start_node,end_node)}')
  # print(f'Bidirectional Heuristic Search Path: {get_bidirectional_heuristic_search_path(adj_matrix,node_attributes,start_node,end_node)}')
  # print(f'Bonus Problem: {bonus_problem(adj_matrix)}')