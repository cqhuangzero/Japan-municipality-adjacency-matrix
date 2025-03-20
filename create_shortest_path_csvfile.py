import numpy as np
import pandas as pd
import networkx as nx
from tqdm import tqdm

# Read the adjacency matrix
adj_matrix = pd.read_csv("D:\\desktop\\map\\adj.csv", index_col=0, encoding="utf-8")

# Ensure index integrity
nodes_list = list(adj_matrix.index)
num_nodes = len(nodes_list)

# Create a NetworkX graph
G = nx.Graph()

# Add all nodes
G.add_nodes_from(nodes_list)

# Iterate through the adjacency matrix and add edges
for i in range(num_nodes):
    for j in range(num_nodes):
        if adj_matrix.iloc[i, j] == 1:
            G.add_edge(nodes_list[i], nodes_list[j])

# Initiate the matrix
shortest_path_matrix = np.full((num_nodes, num_nodes), -1, dtype=np.int16)

# Count the shortest route by BFS
for i, source in tqdm(enumerate(nodes_list), total=num_nodes, desc="Calculating shortest paths"):
    lengths = nx.single_source_shortest_path_length(G, source)
    for target, dist in lengths.items():
        j = nodes_list.index(target)
        shortest_path_matrix[i, j] = dist

# Convert into DataFrame
shortest_path_df = pd.DataFrame(shortest_path_matrix, index=nodes_list, columns=nodes_list)

# Save as CSV
shortest_path_df.to_csv("D:\\desktop\\map\\shortest_paths.csv", encoding="utf-8")
