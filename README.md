Búsqueda de Usuarios

Este proyecto genera una lista de 100,000 usuarios con datos aleatorios (nombre, ID, Edad). Luego, permite buscar un usuario en la lista utilizando dos métodos diferentes: \*\*búsqueda lineal\*\* y \*\*búsqueda binaria\*\*. También se comparan los tiempos de ejecución de ambos métodos.

- Funcionamiento
1. Generación de usuarios

Cada usuario tiene tres atributos:

- ID: un número único que identifica al usuario.
- Nombre: uno de los nombres seleccionados aleatoriamente de una lista.
- Eda: un número aleatorio entre 18 y 80 años.

Se crean 100,000 usuarios utilizndo estos atributos y se almacenan en una lista llamada usuarios.

2\. Métodos de búsqueda

El código implementa dos funciones de búsqueda, las cuales son:

- Búsqueda lineal: Reciorre toda la lista de usuarios buscando el ID.
- Búsqueda binaria: La lista de usuarios se ordena primero por el ID. Luego, la búsqueda binaria divide la lista en dos partes y sigue buscando en la mitad correspondiente hasta encontrar el usuario.

3\. Comparación de tiempos

Se utiliza el módulo time para medir cuánto tiempo tarda cada tipo de búsqueda en encontrar un usuario con un ID aleatorio.

4\. Cómo utilizar

1. Clonar el repositorio
1. Ejecuta el scrippt
1. Ver el tiempo que tardó cada una.


