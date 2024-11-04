import heapq

def dijkstra(graph, start, end):
    # Diccionario para almacenar la distancia mínima desde el nodo de inicio a cada nodo
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # La distancia desde el nodo de inicio a sí mismo es 0

    # Diccionario para almacenar el camino más corto para reconstruir la ruta al final
    previous_nodes = {node: None for node in graph}

    # Cola de prioridad para seleccionar el nodo con la distancia más corta en cada paso
    priority_queue = [(0, start)]

    while priority_queue:
        # Selecciona el nodo con la distancia más corta
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si hemos alcanzado el nodo final, podemos detenernos
        if current_node == end:
            break

        # Si encontramos una distancia mayor, ignoramos este nodo
        if current_distance > distances[current_node]:
            continue

        # Actualizamos la distancia para cada vecino
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Solo actualizamos la distancia si encontramos un camino más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruimos el camino más corto
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path = path[::-1]  # Invertimos el camino para obtenerlo en el orden correcto

    return path, distances[end]  # Retorna el camino y la distancia mínima


graph = {
    'A': {'B': 45, 'C': 100},
    'B': {'A': 45, 'D': 60, 'E': 85},
    'C': {'A': 100, 'D': 120},
    'D': {'B': 60, 'C': 120, 'E': 50},
    'E': {'B': 85, 'D': 50}
}

start = 'A'
end = 'E'
path, cost = dijkstra(graph, start, end)
print(f"El camino más corto de {start} a {end} es: {path} con un costo total de {cost}")
