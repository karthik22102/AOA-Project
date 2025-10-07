from flask import Flask, render_template, request, jsonify
from bellman_ford import bellman_ford, reconstruct_path
import os
import json

app = Flask(__name__)

# Sample network topology
network_topology = {
    'Router_A': {'Router_B': 10, 'Router_C': 15},
    'Router_B': {'Router_A': 10, 'Router_D': 20, 'Server_1': 5},
    'Router_C': {'Router_A': 15, 'Router_D': 25, 'Server_2': 8},
    'Router_D': {'Router_B': 20, 'Router_C': 25, 'Internet_Gateway': 30},
    'Server_1': {'Router_B': 5},
    'Server_2': {'Router_C': 8},
    'Internet_Gateway': {'Router_D': 30}
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/calculate-path', methods=['POST'])
def calculate_path():
    data = request.json
    source = data['source']
    target = data['target']

    distances, predecessors = bellman_ford(network_topology, source)

    if distances is None:
        return jsonify({'error': 'Negative cycle detected'})

    if distances[target] == float('infinity'):
        return jsonify({'error': 'No path exists'})

    path = reconstruct_path(predecessors, target)

    return jsonify({
        'path': path,
        'total_latency': distances[target],
        'all_distances': distances
    })


@app.route('/api/network-topology')
def get_topology():
    return jsonify(network_topology)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
