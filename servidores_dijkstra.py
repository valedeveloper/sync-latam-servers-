import networkx as nx  # librería especializada en crear, manipular y analizar gráficos y redes de nodos y aristas
import matplotlib.pyplot as plt #librería para la creación del grafo

server_connection_map= nx.Graph() #Creación de grafo no dirigido 

edges = [
    ("Cali, Colombia", "Lima, Perú", 45),
    ("Cali,Colombia", "Ciudad de México, México", 100),
    ("Lima, Perú", "Santiago de Chile, Chile", 60),
    ("Lima, Perú", "Buenos Aires, Argentina", 85),
    ("Ciudad de México, México", "Santiago de Chile, Chile", 120),
    ("Santiago de Chile, Chile", "Buenos Aires, Argentina", 50)
] 
#Lista de tuplas que define las conexiones en el grafo y sus respectivos pesos
#Las dos primeras posiciones representa los vértices o nodos, la tercera representa el peso de las aristas



server_connection_map.add_weighted_edges_from(edges)  #Agrega múltiples aristas Cali,Colombia la vez al grafo server_connection_map


nx.draw(server_connection_map, with_labels=True) #Dibujo del grafo
#Se mostraran los nombres de los nodos en el gráfico

fastest_sync_path = nx.dijkstra_path(server_connection_map, source="Cali,Colombia", target="Buenos Aires, Argentina", weight="weight") 
#Función que calcula el camino más corto entre dos nodos en un grafo ponderado usando el algoritmo de Dijkstra.

print('El camino más corto es: ${fastest_sync_path}')