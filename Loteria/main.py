import random
import pandas as pd

cardusadas=[]
errores=0
casillas=16

def baraja ():
  global cardusadas
  lst=(range(1,55)) #Ya no se usa
  while True:
    n = random.randrange(1, 55)
    if n not in cardusadas:
      cardusadas.append(n)
      break
    else:
        False
  return n

def tabla ():
  tablas=pd.read_csv('Loteria.csv',header=0)
  while True:
    sectabla=int(input("Seleccione su tabla de 1-24: "))
    eleccion=(tablas['Tabla (sectabla)'])
    print (eleccion)
    decision=int(input("¿Desea quedarse con esta tabla?"))
    print ("1. Si")
    print ("2. No")
    sn=int(input())
    if sn==1:
      return eleccion
    elif sn==2:
      False
    else:
      print ("Error, seleccione de nuevo")
      False
            
def fin_del_juego(): #Aun no terminado
  global errores
  puntuacion=100000-(errores*100)
  print("La puntación fue:", puntuacion)
  
def seleccion(tabla, fila, columna):
  global cardusadas
  global casillas
  global errores
  seleccion=int(tabla[fila][columna])
  if seleccion=="*":
    print("Piedra ya fue colocada en este espacio")
    errores+=1
  elif seleccion in cardusadas:
    seleccion="*"
    casillas=casillas-1
  else:
    print("Este número no ha pasado")
    errores+=1
  if casillas==0:
    fin_del_juego()