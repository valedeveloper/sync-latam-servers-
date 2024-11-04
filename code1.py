import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo dirigido
G = nx.Graph()

# Añadir los nodos al grafo
nodes = {
    "A": "Cali, Colombia",
    "B": "Lima, Perú",
    "C": "Ciudad de México, México",
    "D": "Santiago de Chile, Chile",
    "E": "Buenos Aires, Argentina"
}

# Añadir los nodos al grafo
for key, value in nodes.items():
    G.add_node(key, label=value)

# Añadir las aristas con los pesos
edges = [
    ("A", "B", 45),
    ("A", "C", 100),
    ("B", "D", 60),
    ("B", "E", 85),
    ("C", "D", 120),
    ("D", "E", 50)
]

# Añadir las conexiones al grafo
G.add_weighted_edges_from(edges)

# Definir posiciones de los nodos para visualización
pos = {
    "A": (0, 2),
    "B": (1, 1),
    "C": (2, 2),
    "D": (1, 0),
    "E": (2, 0)
}

# Dibujar el grafo
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), node_color="skyblue", node_size=3000, font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d} ms" for u, v, d in edges}, font_color="red", font_size=10)
plt.title("Grafo de Sincronización de Repositorios en Latinoamérica")
plt.show()
