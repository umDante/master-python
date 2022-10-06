# import pdb
# pdb.set_trace()


# USAR COMANDO PARA EJECUTAR: python -m pdb main.py

"""
Actividad relacionada con la lección 4:

    1. Haciendo uso de comprensión de listas realice un programa que, dado
    una lista de listas de números enteros, devuelva el máximo de cada
    lista. Por ejemplo, suponga la siguiente listas de listas:
    [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
    El programa debe devolver el mayor elemento de cada sublista
    (señalado en negrita).
    Ahora, haciendo uso del pdb, inserte puntos de parada justo en la línea
    donde ha implementado la compresión de listas. Haga pruebas
    mostrando el contenido de las variables y continuar con la ejecución
    línea a línea. ¿Qué conclusiones obtiene?
    
    2. Haga uso de la función filter para construir un programa que, dado
    una lista de n números devuelva aquellos que son primos. Por
    ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente
    debe devolver como resultado [3, 5, 5, 13]
"""


# # # # # # # # # # # # # PUNTO 1: SOLUCIÓN CON COMPRENSIÓN # # # # # # # # # # # # # # # # 
# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#

data = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
mayores = [ item for items in data for item in items if item == max(items)]
print(mayores)



# # # PUNTO 1: SOLUCIÓN CON map y lamba
# mayores =list(map(lambda d: max(d), data))
# print(mayores)



# # # PUNTO 1:  SOLUCIÓN CON ARREGLO DE FUNCIONES
# def getLista(lista):
#         return lista 

# def getMayor(lista):
#     return f"  mayor --> {max(lista)}"


# funciones = [getLista, getMayor]

# for e in data:
#     valores = list(map(lambda x : x(e), funciones))
#     print(f" {valores}")


# USAR COMANDO PARA EJECUTAR: python -m pdb main.py
    # n para seguir a linea siguiente (Pdb) n
    # nombre_de_variabe "luego de ejecutarse " para ver contenido (Pdb) mayores


# # # # # # # # # # # # # PUNTO 2: SOLUCIÓN CON FILTER # # # # # # # # # # # # # # # # 
# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#

def es_primo(item):
    for n in range(2, item):
        if item % n == 0:
            print(f"El número {item} NO es primo")
            return False
    print(f"El número {item} SI es primo")
    return True

    
lista = [3, 4, 8, 5, 5, 22, 13]

primos = list(filter(es_primo, lista))
print(primos)