# Mutantes

* Mateo De Martino
* 51521
* mateodemartino@gmail.com

## Tema del Proyecto

El proyecto consta de un sistema de verificación de mutaciones en secuencias de ADN, permitiendo al usuario ingresar múltiples secuencias y determinando si hay mutaciones siguiendo reglas específicas. La estructura modular del código facilita la comprensión y la capacidad de mantenimiento.

## Como se resolvio

El código utiliza una estructura con dos funciones principales: "main" y "mutante". La primera gestiona la entrada de datos del usuario, asegurándose de que las secuencias ingresadas cumplan con criterios específicos. La segunda función, "mutante", realiza la verificación de mutaciones en la matriz de ADN, buscando coincidencias en filas, columnas y diagonales. El programa determina si una secuencia es mutante si encuentra más de una mutación en las direcciones especificadas. El enfoque iterativo del código permite una implementación eficiente y la estructura clara facilita la comprensión del proceso de verificación de mutaciones en el contexto de la biología molecular. 

## Ejecución
En la consola correr el siguiente comando
(verifique que tenga anteriormente instalado python 3.9 o posteriores)

    python3 mutantes.py    