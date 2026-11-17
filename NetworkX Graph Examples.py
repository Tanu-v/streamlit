from __future__ import annotations
from typing import Callable
import streamlit as st
import networkx as nx
from streamlit_extras.sigma_graph import sigma_graph

st.write("### NetworkX Graph Examples")
st.write("Explore different graph datasets and generators from NetworkX.")

# Graph options - mix of classic graphs and parameterized generators
graph_options: dict[str, Callable[[], nx.Graph]] = {
    "Karate Club (34 nodes)": nx.karate_club_graph,
    "Les Misérables (77 nodes)": nx.les_miserables_graph,
    "Florentine Families (15 nodes)": nx.florentine_families_graph,
    "Barabási-Albert (500 nodes)": lambda: nx.barabasi_albert_graph(500, 3),
    "Barabási-Albert (1000 nodes)": lambda: nx.barabasi_albert_graph(1000, 2),
    "Watts-Strogatz (500 nodes)": lambda: nx.watts_strogatz_graph(500, 4, 0.3),
    "Random Geometric (400 nodes)": lambda: nx.random_geometric_graph(400, 0.1),
}

layout_options: dict[str, str] = {
    "Force (ForceAtlas2)": "force",
    "Spring (Fruchterman-Reingold)": "spring",
    "Circular": "circular",
    "Kamada-Kawai": "kamada_kawai",
    "Random": "random",
}

size_options: dict[str, int | str | None] = {
    "By degree (connections)": "degree",
    "Uniform (8)": 8,
    "Uniform (12)": 12,
}

col1, col2, col3 = st.columns(3)
with col1:
    selected_graph = st.selectbox(
        "Select a graph",
        options=list(graph_options.keys()),
        key="networkx_graph_selector",
    )
with col2:
    selected_layout = st.selectbox(
        "Layout algorithm",
        options=list(layout_options.keys()),
        key="networkx_layout_selector",
    )
with col3:
    selected_size = st.selectbox(
        "Node sizing",
        options=list(size_options.keys()),
        key="networkx_size_selector",
    )

# Load the selected graph
graph_fn = graph_options[selected_graph]
graph = graph_fn()
layout = layout_options[selected_layout]
node_size = size_options[selected_size]

# Add labels only for smaller graphs
if graph.number_of_nodes() <= 100:
    for node in graph.nodes:
        graph.nodes[node]["label"] = str(node)

st.caption(f"**{graph.number_of_nodes()}** nodes, **{graph.number_of_edges()}** edges")
sigma_graph(graph, layout=layout, node_size=node_size, height=550)
