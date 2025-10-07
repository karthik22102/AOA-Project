def bellman_ford(graph, source):
    """
    Implementation of Bellman-Ford algorithm for shortest path
    """
    # Initialize distances and predecessors
    distance = {node: float('infinity') for node in graph}
    predecessor = {node: None for node in graph}
    distance[source] = 0

    print("Initial distances:", distance)

    # Relax edges |V| - 1 times
    for i in range(len(graph) - 1):
        print(f"\n--- Iteration {i+1} ---")
        updated = False

        for u in graph:
            for v, weight in graph[u].items():
                print(f"Checking edge {u} -> {v} (weight: {weight})")
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u
                    updated = True
                    print(f"  Updated {v}: new distance = {distance[v]}")

        if not updated:
            print("No updates in this iteration - early termination")
            break

    # Check for negative cycles
    print("\n--- Checking for negative cycles ---")
    for u in graph:
        for v, weight in graph[u].items():
            if distance[u] + weight < distance[v]:
                print("❌ Negative cycle detected!")
                return None, None

    print("✅ No negative cycles found")
    return distance, predecessor


def reconstruct_path(predecessor, destination):
    """
    Reconstruct the path from source to destination
    """
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = predecessor[current]

    path.reverse()
    return path


def print_network_graph(graph):
    """
    Display the network topology
    """
    print("\n🌐 Network Topology:")
    print("-" * 30)
    for node in graph:
        connections = []
        for neighbor, weight in graph[node].items():
            connections.append(f"{neighbor}({weight}ms)")
        print(f"{node}: {', '.join(connections)}")
    print("-" * 30)
