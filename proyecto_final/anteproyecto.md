# Comparación algoritmo genético y A* en recorrido óptimo Uber

## "UBAE"

## Integrantes: 
Fabricio Espejo 13223.  
Cristian Serrano 13081.

## Idea general.

El objetivo de este proyecto es estudiar a fondo la funcionalidad de los algoritmos A* y genético vistos en la cátedra para observar resultados, comparar los mismos, implementarlos con las modificaciones que se requiera y crear el funcionamiento interno de una aplicación basada en la ya conocida *"Uber"*. Donde funcionamiento interno se refiere a seleccionar el camino más óptimo desde un punto de partida (ubicación del conductor) hasta uno intermedio (ubicación del cliente) para luego desplazarse al destino.

Se ejecutarán ambos algoritmos sobre varios conjuntos de datos reales sobre calles y tráfico de USA. Dichos datos serán previamente analizados y modelados de la forma más conveniente posible para que se adapten al problema propuesto. La metodología será testear los algoritmos en cada conjunto de datos sobre una cantidad proporcional de caminos distintos y comparar resultados para ver si nos conviene utilizar dichos algoritmos, cómo deberíamos hacerlo y si nos es más eficiente reemplazar alguno o no.

Ambos algoritmos seleccionados tienen sus desventajas y ventajas, por ejemplo, la limitación que tiene el algoritmo genético es que, al ser un algoritmo del tipo greedy, no siempre llega a la solución u objetivo pero obtiene una buena aproximación en un tiempo relativamente corto. Y el algoritmo A* no es muy eficiente cuando se trata de recorridos extremadamente largos, ya que, al ser completo, busca el camino correcto lo que implica recorrer todos los nodos posibles y calcular la heurística para al menos todos ellos. Lo que es una limitación para grafos muy grandes se convierte en una ventaja para grafos pequeños donde siempre encontrará la solución en un tiempo muy corto (dependiendo de la heurística que se tenga en cuenta).

Las métricas serán evaluadas en el tiempo de ejecución, la cantidad de estados recorridos y las veces que llega a un estado satisfactorio en cada uno de los conjuntos de datos, una vez recopilada la información, realizar una tabla comparando ambos algoritmos y tomar decisiones sobre qué parámetros ajustar en el algoritmo genético y cuándo aplicar el A*.

Los problemas de búsqueda en árboles o grafos es algo que lleva un costo computacional muy alto, especialmente en las metodologías tradicionales donde en el peor de los casos se recorre casi toda la estructura si no es que toda antes de encontrar la solución. Sin embargo, al utilizar los algoritmos de IA se le da una inteligencia extra a la máquina para que sepa por donde ir hasta llegar a la solución sin la necesidad de recorrer la mayoría de los nodos, haciendo mucho más eficiente y rápido el trabajo.

## Actividades.

__1:__ Recopilacion de datos y mapas [2 días]

__2:__ Adaptar datos al problema [5 días]

__3:__ Implementación de A* [3 días]

__4:__ Ejecutar A* [2 días]

__5:__ Implementación del algoritmo genético [4 días]

__6:__ Ejecutar Genético [2 días]

__7:__ Ajustes y correciones [5 días]

__8:__ Analizar y comparar los resultados [2 días]  

__9:__ Elaborar informe final [20 días]

## Cronograma estimado de actividades

<img src="./Cronograma.png"/>

## Bibliografia

Se consultó el libro AIMA 2da Edition(español) y 3rd edition.

[Para consumir los datos reales](http://www.diag.uniroma1.it//challenge9/download.shtml)
