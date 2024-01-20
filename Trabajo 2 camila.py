
mi_variable= "Hola a todos c:"
print (mi_variable)

#Lista de notas decantes
mi_lista=[5,6,4,3,2]
print(mi_lista)

#Diccionario sobre mis datos personales
mi_diccionario={"Nombre":"Alexis", "Edad":"22", "Signo zodiacal":"Escorpio"}
print(mi_diccionario)

####################################
#Declarar un vector de enteros

#Numerica
#Vector de enteros sobre mi numero favorito 
vector_enteros = [2]*11
print(vector_enteros)

#Vestor de enteros sobre el numero de euler
vector_flotantes=[2.71]*11
print(vector_flotantes)

diccionario = {"entero" : vector_enteros, "florante": vector_flotantes}
print(diccionario)

#cadenas
#salidas y mensajes, interpretacion con el usuario
#cracion de identificadores

cadena_simple = 'Buenas noches compañeros!'

#contener dos variables de texto
#Top 2 de series favs
cadena_doble = ["GOT","Breaking Bad"]
print(cadena_doble)
print(cadena_simple)

#librerias
import pandas as pd

#Importar datos
imp_sri =pd.read_excel("data/ipc.xlsx")
print(imp_sri)