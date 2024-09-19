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
# - The expected output for each function is a path (list of node names)
# - Ensure that the returned path includes both the start node and the goal node, in the correct order.
# - If no valid path exists between the start and goal nodes, the function should return [].


# Algorithm: Iterative Deepening Search (IDS)

# Input:
#   - adj_matrix: Adjacency matrix representing the graph.
#   - start_node: The starting node in the graph.
#   - goal_node: The target node in the graph.

# Return:
#   - A list of node names representing the path from the start_node to the goal_node.
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
  stack=[]
  stack.append([start_node,[start_node],0])
  result = []
  visited = set()       #made a visited to optimize the code
  while(len(stack)>0):
    # print(stack)
    list=stack.pop()
    node=list[0]
    path=list[1]
    depth=list[2]
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
  for i in range(0,33):
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
#   - A list of node names representing the path from the start_node to the goal_node.
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
#   - A list of node names representing the path from the start_node to the goal_node.
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
#   - A list of node names representing the path from the start_node to the goal_node.
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
# - adj_matrix: A 2D list or numpy array representing the adjacency matrix of the graph.

# Return:
# - A list of tuples where each tuple (u, v) represents an edge between nodes u and v.
#   These are the vulnerable roads whose removal would first_foundonnect parts of the graph.

# Note:
# - The graph is undirected, so if an edge (u, v) is vulnerable, then (v, u) should not be repeated in the output list.
# - If the input graph has no vulnerable roads, return an empty list [].

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

if __name__ == "__main__":
  adj_matrix = np.load('Assignment_1\IIIT_Delhi.npy')
  with open('Assignment_1\IIIT_Delhi.pkl', 'rb') as f:
    node_attributes = pickle.load(f)

  # print(sum(adj_matrix[1]))
  start_node = int(input("Enter the start node: "))
  end_node = int(input("Enter the end node: "))
  # start_node = 1
  # end_node = 2

  # l=[]
  # for start_node in range(125):
  #   for end_node in range(125):
  #     print(f'Start Node: {start_node}, End Node: {end_node}')
  #     temp1=get_ids_path(adj_matrix,start_node,end_node)
  #     # print(temp1)
  #     temp2=get_bidirectional_heuristic_search_path(adj_matrix,node_attributes,start_node,end_node)
  #     if(temp1==[] and temp2!=[]):
  #       l.append([start_node,end_node])
  #       break
  #     if(temp1!=[] and temp2==[]):
  #       l.append([start_node,end_node])
  #       break
  #   else:
  #     print('success')
  # print('complete')
  # print(l)
  
  
  print(f'Iterative Deepening Search Path: {get_ids_path(adj_matrix,start_node,end_node)}')
  print(f'Bidirectional Search Path: {get_bidirectional_search_path(adj_matrix,start_node,end_node)}')
  print(f'A* Path: {get_astar_search_path(adj_matrix,node_attributes,start_node,end_node)}')
  print(f'Bidirectional Heuristic Search Path: {get_bidirectional_heuristic_search_path(adj_matrix,node_attributes,start_node,end_node)}')
  print(f'Bonus Problem: {bonus_problem(adj_matrix)}')