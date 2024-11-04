<h1>🌐 Proyecto de Sincronización de Servidores en América Latina 🌐</h1>

<p>Estudio de la ruta óptima de sincronización de datos entre servidores Git en diferentes ciudades de América Latina, usando el Algoritmo de Dijkstra.</p>

<h2>📚 Descripción del Caso de Estudio</h2>
<p>Este proyecto explora cómo sincronizar datos entre varios servidores distribuidos en diferentes ciudades latinoamericanas para minimizar el tiempo de actualización entre ellos. Utilizando el Algoritmo de Dijkstra, calculamos la ruta más rápida para la sincronización de información desde Cali, Colombia hasta Buenos Aires, Argentina, pasando por servidores en Perú, México, y Chile.</p>

<h2>🗺️ Nodos y Conexiones</h2>
<p>Los puntos de sincronización clave en este grafo son ciudades de América Latina:</p>

<h3>Nodos (Servidores):</h3>
<ol>
  <li>Cali, Colombia (punto de origen)</li>
  <li>Lima, Perú</li>
  <li>Ciudad de México, México</li>
  <li>Santiago de Chile, Chile</li>
  <li>Buenos Aires, Argentina (punto de destino)</li>
</ol>

<h3>Conexiones (Aristas):</h3>
<p>Cada conexión tiene un peso que representa el tiempo de sincronización en minutos entre servidores (ms), calculado en función de la distancia geográfica y el tiempo de transmisión estimado.</p>

<h2>🎨 Visualización del Grafo</h2>
<p>El grafo a continuación representa las ciudades como nodos y los tiempos de sincronización entre ellos como conexiones (aristas), mostrando la ruta óptima calculada:</p>

![image](https://github.com/user-attachments/assets/08ec6768-1a88-45a2-8299-e54fd5a5c086)


<h2>🏆 Conclusión</h2>
<p>Para optimizar el tiempo de sincronización entre Cali y Buenos Aires, el camino óptimo es: <strong>Cali → Lima → Buenos Aires</strong>. Este trayecto minimiza el tiempo total a 130 minutos, facilitando una sincronización más eficiente.</p>



