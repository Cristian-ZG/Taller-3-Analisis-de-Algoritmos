# Taller-3-Analisis-de-Algoritmos

## Estructura del Taller
![Estrucutra del taller 3.](https://i.imgur.com/bEXLweJ.png)

## Introducción
En el taller 3 de ADA, se utilizó el archivo `main.py` para implementar la
clase *AlgoritmosTester* para realizar ahi los test de los algortimos.

### Asignación de tamaño de los arreglos a utilizar en los test
> [!IMPORTANT]
> Asignar el tamaño del arreglo a utilizar antes de ejecutar el main.py.

El tamaño del arreglo se asigna manualmente en el `main.py` 

````
listn = [random.randint(1, 100) for _ in range(10)]
````
En el codigo se vería así:
![Codigo a cambiar](https://i.imgur.com/fR7KWnp.png)
Donde el `in range(10)` que viene por defecto se cambia por el tamaño del arreglo que desee. `10,100,1000,1000`
### Ejemplo asignando un rango de 1000
Así quedaría 
````
listn = [random.randint(1, 100) for _ in range(1000)]
````
## Ejecucion de los test
Al ejecutar el programa despues del paso anterior, saldrá un menú donde se indica la opcion que se desea ejecutar.


![Consola de ejecucion](https://i.imgur.com/L2qle9J.png)

Despues de elegida la opcion y de pulsar `Enter` dará los resultados de los test según la opcion elegida.

## Autores
>Alejandro Marin Hoyos 2259353-3743
>
> Cristan David Zuñiga 2259425-2724
> 
>Juan Jose Marin Arias 2259337-2724
