## Introducción

Dentro de esta carpeta se encuentra todo el código necesario para ejecutar los algoritmos A* y Genético con el fin de obtener métricas y analizar los resultados de aplicarlos sobre el problema de encontrar el camino óptimo entre los puntos A y B.

Para realizar este experimento, se utilizan datos reales de EE.UU.

## Requisitos

Para poder ejecutar todos los scipts y algoritmos sin ningun inconveniente es necesario tener instalado lo siguiente:

- [NodeJS](https://nodejs.org/es/download) (Versión mínima 18.16.1)

- [Python](https://www.python.org/downloads/) (Versión mínima 3.11.4)

## Estructura del directorio

Dentro de este directorio nos encontramos con 4 carpetas principales las cuales algunas poseen un nivel de complejidad superior y por esto se indican los pasos a seguir dentro de cada una para ejecutar el proceso sin problema alguno.

Ahora bien, dentro de la carpeta `/database` veremos un proyecto NodeJS que se encarga de manejar los datos en una base de datos *SQLite*. ***Cabe destacar que antes de ejecutar cualquier algoritmo, se debe iniciar este servicio***.

Luego, la carpeta `/modules` posee todos los módulos custom extras que veamos convenientes utilizar para cualquier algoritmo.

También existe una carpeta llamada `/test` la cual posee los scripts necesarios para que se puedan ejecutar los algoritmos correspondientes.

Y, finalmente, el código fuente de los algoritmos se encuentran en la raíz de este directorio.