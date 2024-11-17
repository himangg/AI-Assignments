#############
## Imports ##
#############

import pickle
import pandas as pd
import numpy as np
import bnlearn as bn
from test_model import test_model

######################
## Boilerplate Code ##
######################

def load_data():
    """Load train and validation datasets from CSV files."""
    # Implement code to load CSV files into DataFrames
    # Example: train_data = pd.read_csv("train_data.csv")
    train_df = pd.read_csv("train_data.csv")
    # train_df = train_df[:1000]
    # print(train_df)
    val_df = pd.read_csv("validation_data.csv")
    return train_df, val_df

def make_network(df):
    """Define and fit the initial Bayesian Network."""
    # Code to define the DAG, create and fit Bayesian Network, and return the model
    nodes = list(df.columns)
    numNodes = len(nodes)
    edges = []
    for i in range(numNodes):
        for j in range(i+1, numNodes):
            edges.append((nodes[i], nodes[j]))
    graph = bn.make_DAG(edges)
    # bn.plot(graph)

    model = bn.parameter_learning.fit(graph, df)
    # bn.plot(model)
    return model


def make_pruned_network(df):
    """Define and fit a pruned Bayesian Network."""
    # Code to create a pruned network, fit it, and return the pruned model
    
    # Since Route_type is always 3, do we do not need a node for it and we can completely ignore this feature
    nodes = list(df.columns)
    nodes.remove("Route_Type")
    print(nodes)
    numNodes = len(nodes)

    #also we dont need an edge between start node and end node as they are independant to each other
    edges = []
    for i in range(numNodes):
        if(i==0):
            for j in range(i+2, numNodes):
                edges.append((nodes[i], nodes[j]))
        else:
            for j in range(i+1, numNodes):
                edges.append((nodes[i], nodes[j]))
    graph = bn.make_DAG(edges)
    model = bn.parameter_learning.fit(graph, df)

    # edge_strengths = bn.structure_learning.fit(df, methodtype='hc')['model_edges']
    # strong_edges = []
    # for edge in edge_strengths:
    #     if(edge[2] >= 0.5):
    #         strong_edges.append(edge)
    # print(strong_edges)

    # # Create a new DAG with pruned edges
    # pruned_graph = bn.make_DAG([(e[0], e[1]) for e in strong_edges])
    # bn.plot(model)
    return model

def make_optimized_network(df):
    """Perform structure optimization and fit the optimized Bayesian Network."""
    # Code to optimize the structure, fit it, and return the optimized model
    optimized = bn.structure_learning.fit(df, methodtype='hc')
    # print(optimized)
    bn.plot(optimized)
    return optimized

def save_model(fname, model):
    """Save the model to a file using pickle."""
    with open(fname, 'wb') as f:
        pickle.dump(model, f)

def evaluate(model_name, val_df):
    """Load and evaluate the specified model."""
    with open(f"{model_name}.pkl", 'rb') as f:
        model = pickle.load(f)
        correct_predictions, total_cases, accuracy = test_model(model, val_df)
        print(f"Total Test Cases: {total_cases}")
        print(f"Total Correct Predictions: {correct_predictions} out of {total_cases}")
        print(f"Model accuracy on filtered test cases: {accuracy:.2f}%")

############
## Driver ##
############

def main():
    # Load data
    train_df, val_df = load_data()
    # print(train_df.head())
    # print(val_df.head())

    # Create and save base model
    # base_model = make_network(train_df)
    # save_model("base_model.pkl", base_model)

    # # Create and save pruned model
    # pruned_network = make_pruned_network(train_df)
    # save_model("pruned_model.pkl", pruned_network)

    # # Create and save optimized model
    # optimized_network = make_optimized_network(train_df)
    # save_model("optimized_model.pkl", optimized_network)

    # Evaluate all models on the validation set
    # evaluate("base_model", val_df)
    # evaluate("pruned_model", val_df)
    evaluate("optimized_model", val_df)

    # print("[+] Done")

if __name__ == "__main__":
    main()

