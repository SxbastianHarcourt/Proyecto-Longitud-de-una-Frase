# Proyecto Módulo 2 : Longitud de una frase
# Víctor Sebastian Rosales Sánchez

print ('''Bienvenido. 
Ingresa una palabra que tenga entre 4 a 8 caracteres. 
''') # Le damos la bienvenida al usuario y se le indican las condiciones para usar el programa.
# Por comodidad propia, se deja un espacio entre la bienvenida, las indicaciones y la solicutud de ingresar la palabra.

palabra = input('Ingrese su palabra: ') # Se le solicita al usuario que ingrese la palabra, por medio de la variable "palabra".
longitud = len(palabra) # La variable "longitud" emplea la función len(), de forma que esta contenga la cantidad de caracteres presentes "palabra".
    # El programa requiere que se cumplan dos condiciones: que la palabra sea igual o mayor a 4 caracteres, y que sea igual o menor a 8 caracteres.
    # Por lo tanto, se deben de indicar esas condiciones.

if palabra.isdigit(): # Se coloca la condición de que si se ingresan valores numéricos, no se lleva a cabo la ejecución del programa.
    print ('No se aceptan caracteres numéricos.')
    print ('Por favor, ingrese una palabra que cumpla con las condiciones del programa.')
    exit ()

elif palabra.isalpha():
    if longitud < 4 : # Primera condicion: Si la palabra no es mayor a 4 caracteres, se debe de indicar un mensaje de error.
        print ('La palabra',palabra, 'solo tiene', longitud, 'caracteres.')
        faltante = 4 - longitud 
        print ('A su palabra le hacen falta', faltante, 'caracteres.') # Se indica la cantidad de caracteres faltantes para cumplir ls condiciones.
        print ('Por favor, ingrese una palabra que cumpla con las condiciones del programa.') # Mensaje de error.
        exit ()
    
    elif longitud > 8 : # Segunda condición: La palabra debe ser menor a 8 caracteres, sino se debe de indicar un mensaje de error.
        print ('La palabra', palabra, 'tiene', longitud, 'caracteres.')
        restante = longitud - 8
        print ('A su palabra le sobran', restante, 'caracteres.') # Se indica la cantidad de caracteres sobrantes, por los cuales no se cumplen las condiciones.
        print ('Por favor, ingrese una palabra que cumpla con las condiciones del programa.') # Mensaje de error.
        exit ()
    
    else :# Al no cumplirse las condiciones anteriores, solamente queda la opción de que el usuario haya ingresado una palabra que cumpla con las condiciones del programa.
        print ('La palabra', palabra, '(con', longitud, 'caracteres) es válida.') 
        exit ()

else: # Si la palabra cuenta con caracteres alfabéticos y numéricos al mismo tiempo, se imprimirá un mensaje de error.
    print ('Su palabra cuenta con caracteres numéricos.') 
    print ('Por favor, ingrese una palabra que cumpla con las condiciones del programa.') 
    exit ()  
