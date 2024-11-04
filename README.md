🌐 Proyecto de Sincronización de Servidores en América Latina 🌐
Estudio de la ruta óptima de sincronización de datos entre servidores Git en diferentes ciudades de América Latina, usando el Algoritmo de Dijkstra.

📚 Descripción del Caso de Estudio:
Este proyecto explora cómo sincronizar datos entre varios servidores distribuidos en diferentes ciudades latinoamericanas para minimizar el tiempo de actualización entre ellos. Utilizando el Algoritmo de Dijkstra, calculamos la ruta más rápida para la sincronización de información desde Cali, Colombia hasta Buenos Aires, Argentina, pasando por servidores en Perú, México, y Chile.


🗺️ Nodos y Conexiones:
Los puntos de sincronización clave en este grafo son ciudades de América Latina:

Nodos (Servidores):
1. Cali, Colombia (punto de origen)
2. Lima, Perú
3. Ciudad de México, México
4. Santiago de Chile, Chile
5. Buenos Aires, Argentina (punto de destino)

Conexiones (Aristas): Cada conexión tiene un peso que representa el tiempo de sincronización en minutos entre servidores, calculado en función de la distancia geográfica y el tiempo de transmisión estimado.


🏆 Conclusión
Para optimizar el tiempo de sincronización entre Cali y Buenos Aires, el camino óptimo es: Cali → Lima → Buenos Aires. Este trayecto minimiza el tiempo total a 130 minutos, facilitando una sincronización más eficiente.


🎨 Visualización del Grafo

