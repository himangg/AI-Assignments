# Boilerplate for AI Assignment — Knowledge Representation, Reasoning and Planning
# CSE 643

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import networkx as nx
from pyDatalog import pyDatalog
from collections import defaultdict, deque

## ****IMPORTANT****
## Don't import or use any other libraries other than defined above
## Otherwise your code file will be rejected in the automated testing

# ------------------ Global Variables ------------------
route_to_stops = defaultdict(list)  # Mapping of route IDs to lists of stops
trip_to_route = {}                   # Mapping of trip IDs to route IDs
stop_trip_count = defaultdict(int)    # Count of trips for each stop
fare_rules = {}                      # Mapping of route IDs to fare information
merged_fare_df = None                # To be initialized in create_kb()

# Load static data from GTFS (General Transit Feed Specification) files
df_stops = pd.read_csv('GTFS/stops.txt')
df_routes = pd.read_csv('GTFS/routes.txt')
df_stop_times = pd.read_csv('GTFS/stop_times.txt')
df_fare_attributes = pd.read_csv('GTFS/fare_attributes.txt')
df_trips = pd.read_csv('GTFS/trips.txt')
df_fare_rules = pd.read_csv('GTFS/fare_rules.txt')



# ------------------ Function Definitions ------------------

# Function to create knowledge base from the loaded data
def create_kb():
    """
    Create knowledge base by populating global variables with information from loaded datasets.
    It establishes the relationships between routes, trips, stops, and fare rules.
    
    Returns:
        None
    """
    # print(df_stops.head())
    # print(df_stops)
    global route_to_stops, trip_to_route, stop_trip_count, fare_rules, merged_fare_df
    
    # Create trip_id to route_id mapping
    for i in range(len(df_trips)):
        trip_to_route[df_trips['trip_id'][i]] = df_trips['route_id'][i]
        
    
    # for i in range(len(df_trips)):
    #     tripId = df_trips['trip_id'][i]
    #     routeId = df_trips['route_id'][i]
        
    #     if(tripId not in trip_to_route):
    #         trip_to_route[tripId] = []
            
    #     trip_to_route[tripId].append(routeId)
        
    #     if( len(trip_to_route[tripId]) > 1):
    #         print("Error: More than one route for a trip")
        
    # Map route_id to a list of stops in order of their sequence
    for i in range(len(df_stop_times)):
        route_to_stops[trip_to_route[df_stop_times['trip_id'][i]]].append(df_stop_times['stop_id'][i])
    
    # Ensure each route only has unique stops
    for route in route_to_stops:
        route_to_stops[route] = list(set(route_to_stops[route]))
    
    # Count trips per stop
    for i in range(len(df_stop_times)):
        stop_trip_count[df_stop_times['stop_id'][i]]+=1

    # Create fare rules for routes

    # Merge fare rules and attributes into a single DataFrame
    
# create_kb()

# Function to find the top 5 busiest routes based on the number of trips
def get_busiest_routes():
    """
    Identify the top 5 busiest routes based on trip counts.

    Returns:
        list: A list of tuples, where each tuple contains:
              - route_id (int): The ID of the route.
              - trip_count (int): The number of trips for that route.
    """
    ans = []
    dict = {}
    for i in trip_to_route.items():
        tripId = i[0]
        routeId = i[1]
        if(routeId not in dict):
            dict[routeId] = 0
        dict[routeId] += 1
    
    sorted_dict = dict.items()
    sorted_dict = sorted(sorted_dict, key = lambda x: x[1], reverse = True)
    for i in range(5):
        ans.append((sorted_dict[i][0], sorted_dict[i][1]))
    return ans
    pass  # Implementation here
    
# print(get_busiest_routes())

# Function to find the top 5 stops with the most frequent trips
def get_most_frequent_stops():
    """
    Identify the top 5 stops with the highest number of trips.

    Returns:
        list: A list of tuples, where each tuple contains:
              - stop_id (int): The ID of the stop.
              - trip_count (int): The number of trips for that stop.
    """
    ans = []
    dict = {}
    sorted_dict = {}
    sorted_dict = sorted(stop_trip_count.items(), key = lambda x: x[1], reverse = True)
    for i in range(5):
        ans.append((sorted_dict[i][0], sorted_dict[i][1]))
    return ans
    pass  # Implementation here

# print(get_most_frequent_stops())

# Function to find the top 5 busiest stops based on the number of routes passing through them
def get_top_5_busiest_stops():
    """
    Identify the top 5 stops with the highest number of different routes.

    Returns:
        list: A list of tuples, where each tuple contains:
              - stop_id (int): The ID of the stop.
              - route_count (int): The number of routes passing through that stop.
    """
    ans=[]
    dict = {}
    for i in route_to_stops.items():
        routeId = i[0]
        stops = i[1]
        for j in stops:
            if(j not in dict):
                dict[j] = 0
            dict[j] += 1
    sorted_dict = dict.items()
    sorted_dict = sorted(sorted_dict, key = lambda x: x[1], reverse = True)
    for i in range(5):
        ans.append((sorted_dict[i][0], sorted_dict[i][1]))
    return ans
    pass  # Implementation here
# print(get_top_5_busiest_stops())


# Function to identify the top 5 pairs of stops with only one direct route between them
def get_stops_with_one_direct_route():
    """
    Identify the top 5 pairs of consecutive stops (start and end) connected by exactly one direct route. 
    The pairs are sorted by the combined frequency of trips passing through both stops.

    Returns:
        list: A list of tuples, where each tuple contains:
              - pair (tuple): A tuple with two stop IDs (stop_1, stop_2).
              - route_id (int): The ID of the route connecting the two stops.
    """
    ans=[]
    consecutive_stops = []
    for i in route_to_stops.items():
        stops = i[1]
        for j in range(len(stops)-1):
            consecutive_stops.append((stops[j], stops[j+1], i[0]))
    
    
    return ans
    pass  # Implementation here
# print(get_stops_with_one_direct_route())

# Function to get merged fare DataFrame
# No need to change this function
def get_merged_fare_df():
    """
    Retrieve the merged fare DataFrame.

    Returns:
        DataFrame: The merged fare DataFrame containing fare rules and attributes.
    """
    global merged_fare_df
    return merged_fare_df

# Visualize the stop-route graph interactively
def visualize_stop_route_graph_interactive(route_to_stops):
    """
    Visualize the stop-route graph using Plotly for interactive exploration.

    Args:
        route_to_stops (dict): A dictionary mapping route IDs to lists of stops.

    Returns:
        None
    """
    
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add edges between stops based on routes
    for route, stops in route_to_stops.items():
        for i in range(len(stops) - 1):
            G.add_edge(stops[i], stops[i + 1], route=route)
    
    # Create edge trace
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = df_stops.loc[df_stops['stop_id'] == edge[0], ['stop_lon', 'stop_lat']].values[0]
        x1, y1 = df_stops.loc[df_stops['stop_id'] == edge[1], ['stop_lon', 'stop_lat']].values[0]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
    
    # Create node trace
    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = df_stops.loc[df_stops['stop_id'] == node, ['stop_lon', 'stop_lat']].values[0]
        node_x.append(x)
        node_y.append(y)
    
    # Create figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=0.5, color='black'), hoverinfo='none'))
    fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers', marker=dict(size=5, color='blue'), hoverinfo='text'))
    
    # Update layout
    fig.update_layout(title='Stop-Route Graph', showlegend=False, hovermode='closest')
    fig.show()
    
    pass  # Implementation here
# visualize_stop_route_graph_interactive(route_to_stops)

# Brute-Force Approach for finding direct routes
def direct_route_brute_force(start_stop, end_stop):
    """
    Find all valid routes between two stops using a brute-force method.

    Args:
        start_stop (int): The ID of the starting stop.
        end_stop (int): The ID of the ending stop.

    Returns:
        list: A list of route IDs (int) that connect the two stops directly.
    """
    
    ans = []
    for i in route_to_stops.items():
        stops = i[1]
        if(start_stop in stops and end_stop in stops):
            ans.append(i[0])
            
    return ans

    
    pass  # Implementation here
# print(direct_route_brute_force(1, 2))

pyDatalog.create_terms('RouteHasStop, DirectRoute, OptimalRoute, X, Y, Z, R, R1, R2')  

# Adding route data to Datalog  
def add_route_data(route_to_stops):
    """
    Add the route data to Datalog for reasoning.
    Args:
        route_to_stops (dict): A dictionary mapping route IDs to lists of stops.
    Returns:
        None
    """
    for i in route_to_stops.items():
        route = int(i[0])
        stops = i[1]
        for j in stops:
            +RouteHasStop(route, int(j))
    # pass  # Implementation here

# Initialize Datalog predicates for reasoning
def initialize_datalog():
    """
    Initialize Datalog terms and predicates for reasoning about routes and stops.

    Returns:
        None
    """
    pyDatalog.clear()  # Clear previous terms  
    print("Terms initialized: DirectRoute, RouteHasStop, OptimalRoute")  # Confirmation print

    # Define Datalog predicates
    DirectRoute(X, Y, R) <= (RouteHasStop(R, X) & RouteHasStop(R, Y) & (X != Y))
    # OptimalRoute(X, Y, Z, R1, R2) <= (DirectRoute(X, Z, R1) & DirectRoute(Z, Y, R2) & (R1 != R2))

    create_kb()  # Populate the knowledge base
    add_route_data(route_to_stops)  # Add route data to Datalog    

# initialize_datalog()

# Function to query direct routes between two stops
def query_direct_routes(start, end):
    """
    Query for direct routes between two stops.

    Args:
        start (int): The ID of the starting stop.
        end (int): The ID of the ending stop.

    Returns:
        list: A sorted list of route IDs (str) connecting the two stops.
    """
    
    ans = []    
    result = (RouteHasStop(R, start) & RouteHasStop(R, end))
    # print(result)
    for i in result:
        ans.append(i[0])
        # ans.append(R)
    return reversed(sorted(ans))
    # pass  # Implementation here

# print(query_direct_routes(2573, 1177))


# Forward chaining for optimal route planning
def forward_chaining(start_stop_id, end_stop_id, stop_id_to_include, max_transfers):
    """
    Perform forward chaining to find optimal routes considering transfers.
    

    Args:
        start_stop_id (int): The starting stop ID.
        end_stop_id (int): The ending stop ID.
        stop_id_to_include (int): The stop ID where a transfer occurs.
        max_transfers (int): The maximum number of transfers allowed.

    Returns:
        list: A list of unique paths (list of tuples) that satisfy the criteria, where each tuple contains:
              - route_id1 (int): The ID of the first route.
              - stop_id (int): The ID of the intermediate stop.
              - route_id2 (int): The ID of the second route.
    """
    

    
    pass  # Implementation here


# Backward chaining for optimal route planning
def backward_chaining(start_stop_id, end_stop_id, stop_id_to_include, max_transfers):
    """
    Perform backward chaining to find optimal routes considering transfers.

    Args:
        start_stop_id (int): The starting stop ID.
        end_stop_id (int): The ending stop ID.
        stop_id_to_include (int): The stop ID where a transfer occurs.
        max_transfers (int): The maximum number of transfers allowed.

    Returns:
        list: A list of unique paths (list of tuples) that satisfy the criteria, where each tuple contains:
              - route_id1 (int): The ID of the first route.
              - stop_id (int): The ID of the intermediate stop.
              - route_id2 (int): The ID of the second route.
    """
    pass  # Implementation here

# PDDL-style planning for route finding
def pddl_planning(start_stop_id, end_stop_id, stop_id_to_include, max_transfers):
    """
    Implement PDDL-style planning to find routes with optional transfers.

    Args:
        start_stop_id (int): The starting stop ID.
        end_stop_id (int): The ending stop ID.
        stop_id_to_include (int): The stop ID for a transfer.
        max_transfers (int): The maximum number of transfers allowed.

    Returns:
        list: A list of unique paths (list of tuples) that satisfy the criteria, where each tuple contains:
              - route_id1 (int): The ID of the first route.
              - stop_id (int): The ID of the intermediate stop.
              - route_id2 (int): The ID of the second route.
    """
    pass  # Implementation here

# Function to filter fare data based on an initial fare limit
def prune_data(merged_fare_df, initial_fare):
    """
    Filter fare data based on an initial fare limit.

    Args:
        merged_fare_df (DataFrame): The merged fare DataFrame.
        initial_fare (float): The maximum fare allowed.

    Returns:
        DataFrame: A filtered DataFrame containing only routes within the fare limit.
    """
    pass  # Implementation here

# Pre-computation of Route Summary
def compute_route_summary(pruned_df):
    """
    Generate a summary of routes based on fare information.

    Args:
        pruned_df (DataFrame): The filtered DataFrame containing fare information.

    Returns:
        dict: A summary of routes with the following structure:
              {
                  route_id (int): {
                      'min_price': float,          # The minimum fare for the route
                      'stops': set                # A set of stop IDs for that route
                  }
              }
    """
    pass  # Implementation here

# BFS for optimized route planning
def bfs_route_planner_optimized(start_stop_id, end_stop_id, initial_fare, route_summary, max_transfers=3):
    """
    Use Breadth-First Search (BFS) to find the optimal route while considering fare constraints.

    Args:
        start_stop_id (int): The starting stop ID.
        end_stop_id (int): The ending stop ID.
        initial_fare (float): The available fare for the trip.
        route_summary (dict): A summary of routes with fare and stop information.
        max_transfers (int): The maximum number of transfers allowed (default is 3).

    Returns:
        list: A list representing the optimal route with stops and routes taken, structured as:
              [
                  (route_id (int), stop_id (int)),  # Tuple for each stop taken in the route
                  ...
              ]
    """
    pass  # Implementation here


