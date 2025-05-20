'''
Programa que ingresando un listado de canciones, cantidad de cartones y cantidad de canciones por carton genere aleatoriamente esos cartones
'''
import random 
def bingo ( canciones , cant_cartones, cant_canciones):
    canciones = canciones.split(";")
    for i in range(1,cant_cartones):
        print(f"Carton {i}: \n  {random.sample(canciones,cant_canciones)}")


canciones = input("Ingrese un listado de las canciones separadas con ; \n ")
cant_cartones = int(input("Ingrese la cantidad de cartones que quiere generar: \n "))
cant_canciones = int(input("Ingrese la cantidad de canciones  que quiere en cada carton:\n "))
bingo(canciones, cant_cartones, cant_canciones)