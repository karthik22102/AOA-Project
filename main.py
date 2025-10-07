from bellman_ford import bellman_ford, reconstruct_path, print_network_graph


def main():
    # Sample network topology (router connections with latency in ms)
    network_topology = {
        'Router_A': {'Router_B': 10, 'Router_C': 15},
        'Router_B': {'Router_A': 10, 'Router_D': 20, 'Server_1': 5},
        'Router_C': {'Router_A': 15, 'Router_D': 25, 'Server_2': 8},
        'Router_D': {'Router_B': 20, 'Router_C': 25, 'Internet_Gateway': 30},
        'Server_1': {'Router_B': 5},
        'Server_2': {'Router_C': 8},
        'Internet_Gateway': {'Router_D': 30}
    }

    print("🚀 Network Latency Calculator")
    print("=" * 50)

    # Display network topology
    print_network_graph(network_topology)

    # Get user input
    print("\nAvailable nodes:", list(network_topology.keys()))

    source = input("Enter source node: ").strip()
    target = input("Enter target node: ").strip()

    # Validate input
    if source not in network_topology or target not in network_topology:
        print("❌ Error: Invalid node names!")
        return

    print(f"\nCalculating optimal path from {source} to {target}...")

    # Run Bellman-Ford algorithm
    distances, predecessors = bellman_ford(network_topology, source)

    if distances is None:
        print("Calculation failed due to negative cycles")
        return

    # Display results
    print("\n" + "=" * 50)
    print("📊 RESULTS")
    print("=" * 50)

    if distances[target] == float('infinity'):
        print(f"❌ No path exists from {source} to {target}")
    else:
        path = reconstruct_path(predecessors, target)
        print(f"📍 Optimal Path: {' → '.join(path)}")
        print(f"⏱️  Total Latency: {distances[target]} ms")

        # Show all distances from source
        print(f"\n📈 Latencies from {source}:")
        for node, dist in distances.items():
            if dist != float('infinity'):
                print(f"   {node}: {dist} ms")
            else:
                print(f"   {node}: unreachable")


if __name__ == "__main__":
    main()
