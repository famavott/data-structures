"""Implementation of Dijkstra's Shortest Path Algorithm."""
from graph_3 import Graph


def dijkstra(graph, start, end, visited=[], distances={}, routes={}):
    """Function utilizing Dijkstra's algorithm.

    Find the shortest path from a starting node to and end node.
    """
    if start == end:
        shortest_path = []
        path_str = ''
        pred = end
        while pred is not None:
            shortest_path.append(pred)
            path_str += pred
            pred = routes.get(pred, None)
        print(shortest_path[::-1])
        return shortest_path[::-1]
    else:
        if not visited:
            distances[start] = 0
        for edge in graph.nodes[start]:
            if edge not in visited:
                new_distance = distances[start] + graph.nodes[start][edge]
                if new_distance < distances.get(edge, float('inf')):
                    distances[edge] = new_distance
                    routes[edge] = start
        visited.append(start)
        unvisited = {}
        for node in graph.nodes:
            if node not in visited:
                unvisited[node] = distances.get(node, float('inf'))
        new_start = min(unvisited, key=unvisited.get)
        dijkstra(graph, new_start, end, visited, distances, routes)
