"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    if start not in graph:
        return[]

    visited = set()
    traversal_order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

def display_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")

def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")
    display_graph(graph)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    start_node = "A"
    traversal = bfs(graph, start_node)

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")
    print(f"Starting node: {start_node}")
    print(f"Traversal order: {traversal}")

    graph["F"].append("G")
    graph["G"] = ["F"]

    print("\n=== UPDATED GRAPH ===")
    display_graph(graph)

    updated_traversal = bfs(graph, start_node)

    print("\n=== UPDATED BFS ===")
    print(f"Starting node: {start_node}")
    print(f"Traversal order: {updated_traversal}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Start from a different node.
    different_start = "D"
    print(
        f"1. Starting from a different node: {different_start}): "
        f"{bfs(graph, different_start)}"
    )

    # Edge case 2: use disconnected graph.
    disconnected_graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
    }

    print("\nDisconnected graph:")
    display_graph(disconnected_graph)
    print(
        "Starting from A:",
        bfs(disconnected_graph, "A"),
        "(C and D are not reached because they are disconnected."
    )

    # Edge case 3: Missing starting node.
    print("\nMissing starting node:")
    print("Starting from Z:", bfs(graph, "Z"))

    # Edge case 4: A graph containing only one node.
    single_node_graph = {
        "X": []
    }

    print("\nGraph containing only one node:")
    print("Starting from X:", bfs(single_node_graph, "X"))

    # Edge case 5: Empty graph.
    empty_graph = {}

    print("\nEmpty graph:")
    print("Starting from A:", bfs(empty_graph, "A"))

if __name__ == "__main__":
    main()
