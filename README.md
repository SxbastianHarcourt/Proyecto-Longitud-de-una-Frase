# Proyecto Módulo 2: Longitud de una Frase
**Creador:** Víctor Sebastian Rosales Sánchez

## ¿Qué se requiere? 💻
* Contar con una computadora/laptop y conexión a internet.
* Tener instalada la última versión de Python.
* Emplear Visual Studio Code como editor de texto.
* Tener descargado Git y vincular nuestro editor de texto a éste.

## Descripción del Proyecto 🧐
El programa tiene el objetivo de cuantificar los caracteres alfabéticos presentes en una palabra ingresada por el usuario, sin embargo, el programa no puede aceptar caracteres numéricos.

Primero es importante darle una bienvenida al usuario, así como indicarle qué características debe de cumplir para ejecutarlo de forma correcta.

**Condiciones del programa:**
* La palabra debe de ser mayor o igual a 4 caracteres alfabéticos.
* La palabra debe de ser menor o igual a 8 caracteres alfabéticos.
* La palabra no debe de tener caracteres numéricos.

Se le debe pedir al usuario que ingrese la palabra seleccionada por medio de la funcion 'input ( )' y asignarla en una variable denominada 'palabra'. 
Posteriomente, una variable denominada 'longitud' va a contener la cantidad de caracteres presentes en la palabra, esto gracias a la función 'len( )', la cual permite conocer la cantidad de caracteres presentes en la palabra.

En primera instancia, se coloca la condición ('if : ') de que si los caracteres son de tipo numérico ('.isdigit( )') **NO** se lleve a cabo la ejecuión del programa, imprimiendo un mensaje en el que se indque que no se aceptan caracteres numéricos y que nuevamente ingrese una palabra que cumpla con las condiciones establecidas.

Si esa condición no se cumple, sigue la condición ('elif : ') de que si los caracteres son de tipo alfabético ('.isalpha( )') se lleve a cabo:

   **1.** La condición de que si la palabra es **menor** a 4 caracteres, se detenga el programa y se imprima un mensaje en el que se indique que la palabra             ingresada no cuenta con los caracteres requeridos, así como los caracteres faltantes para que esta sea válida.

   **2.** La condición de que si la palabra es **mayor** a 8 caracteres, se detenga el programa y se imprima un mensaje en que se indique que la palabra                 ingresada tiene un exceso de caracteres, así como la cantidad de caracteres sobrantes por los cuales no es válida.

   **3.** Si no se cumplen las condiciones anteriores, solo queda la opcion de que la palabra ingresada contenga de entre 4 a 8 caracteres, por lo que ésta             sería válida. Si esta opción se cumple, se imprime un mensaje en el que se indique que la palabra ingresada cumple con las condiciones estipuladas,           siendo así válida.

Sin embargo, existe la posibilidad de que no se cumpla ninguna de las condiciones anteriores, es decir, que se ingrese una palabra que cuente con carateres numéricos y alfabéticos ('else ( )'). Si esto sucede, se debe imprimir un mensaje el cual indique la palabra ingresada cuenta con caracteres numéricos y alfabéticos, por lo cual esta no es válida.

## ¿Qué me ha dejado el Bootcamp? 🚀
Con este proyecto pude dame cuenta que el BootCamp me ha permitido comprender cómo hacer la correcta asignación de variables, así como el ingreso y solicitud de datos. Así mismo, he aprendido cómo 'castear' y obtener información a partir de los datos presentes a cada variable, y a partir de estos, establecer condiciones en el programa, de forma que se ejecuten condiciones específicas para cada posible situación que el usuario cometa, de forma que se cumpla con el objetivo y propósito del programa. Con todo esto, considero que lo más importante que he aprendido ha sido la organización y distribución de código, de forma que el programa tenga un orden, secuencia, pero sobretodo **coherencia**, para poder ejecutarse correctamente y cumplir con su propósito.
