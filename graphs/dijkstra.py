import networkx
from typing import Dict


def build_demo_graph() -> networkx.Graph:
    graph = networkx.Graph()

    edges = [
        ("A", "B", 1),
        ("A", "C", 4),
        ("B", "C", 2),
        ("B", "D", 5),
        ("C", "D", 1),
    ]

    graph.add_weighted_edges_from(edges)
    return graph


def dijkstra(graph: networkx.Graph, start: str) -> Dict[str, int]:
    return networkx.single_source_dijkstra_path_length(
        graph,
        source=start,
        weight="weight"
    )