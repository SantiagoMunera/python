# Santiago Munera Arango 
# Tatiana Salazar Bedoya
# Maria Antonia Penagos

# FDPM Parcial Virtual

#Escriba un algoritmo que mediante un método le muestre al usuario el siguiente menú de una calculadora:

def menu():
  print("-----------------------------------------------")
  print("----------------- CALCULADORA -----------------")
  print("-----------------------------------------------")
  print()
  print(" Opciones:")
  print()
  print("  1.) SUMAR")
  print("  2.) RESTAR")
  print("  3.) MULTIPLICAR")
  print("  4.) DIVIDIR")
  print("  -------------------------")
  print("  5.) SALIR DE LA CALCULADORA")


def sumando():
  print("----------------- SUMANDO -----------------")
  print()
  n = int(input("¿Cuantos numeros desea sumar?: "))
  print()  
  numero = int(0)
  suma = int(0)

  while(n < 2):
    print(" ALERTA: Debes de sumar 2 o más numeros")
    print()
    n = int(input("¿Cuantos numeros desea sumar?: "))
    print()  

  if (n >= 2):
    for k in range (n):
      k += 1
      print(" NUMERO",k,": ")
      numero = int(input("  - Digite numero:"))
      print()
      suma += numero 

  VECSUMA.append(suma)

def restando():
  print("----------------- RESTANDO -----------------")
  print()
  A = int(input("Digite el primer numero: "))
  B = int(input("Digite el segundo numero: "))
  resta = int(0)
  print()
  resta = A-B

  VECRESTA.append(resta)

def multiplicando():
  print("----------------- MULTIPLICANDO -----------------")
  print()
  n = int(input("¿Cuantos numeros desea multiplicar?: "))
  print()
  numero = int(0)
  multi = int(1)

  while(n < 2):
    print(" ALERTA: Debes de multiplicar por 2 o más numeros")
    print()
    n = int(input("¿Cuantos numeros desea multiplicar?: "))
    print()

  if(n >= 2):
    for k in range (n):
      k += 1
      print(" NUMERO",k,": ")
      numero = int(input("  - Digite numero:"))
      while (numero == 0):
        print()
        print(" ALERTA: No puedes multiplicar por cero")
        print()
        numero = int(input("  - Digite numero:"))
      print()
      multi *= numero 

  VECMULTI.append(multi)  

def dividiendo():
  print("----------------- DIVIDIENDO -----------------")
  print()
  NRO1 = int(input("Digite el numerador: "))
  NRO2 = int(input("Digite el denominador: "))
  while (NRO2 == 0):
    print()
    print(" ALERTA: El denominador no puede ser cero")
    print()
    NRO2 = int(input("Digite el denominador: "))
  divi = int(0)
  print()
  divi = NRO1 / NRO2

  VECDIVI.append(divi)

def Calculadora():
  cont_suma = int(0)
  cont_resta = int(0)
  cont_multi = int(0)
  cont_divi = int(0)

  menu()
  print()
  opcion = int(input("Selecione una Opcion: "))
  
  if (opcion > 0 and opcion < 5):
    while (opcion > 0 and opcion < 5):
      if (opcion == 1):
        cont_suma += 1
        print()
        sumando()
        print()
        menu()
        print()
        opcion = int(input("Selecione una Opcion: "))

      elif(opcion == 2):
        cont_resta += 1
        print()
        restando()
        print()
        menu()
        print()
        opcion = int(input("Selecione una Opcion: "))

      elif(opcion == 3):
        cont_multi += 1
        print()
        multiplicando()
        print()
        menu()
        print()
        opcion = int(input("Selecione una Opcion: "))

      elif(opcion == 4):
        cont_divi += 1
        print()
        dividiendo()
        print()
        menu()
        print()
        opcion = int(input("Selecione una Opcion: "))
        
    if (opcion <= 0 or opcion > 5):
      print()
      print("   ALERTA: No seleccionaste una opcion correcta")
      print()
      reiniciar = str(input("Presione '1' para reiniciar la calculadora: "))
      while (reiniciar != "1"):
        print()
        reiniciar = str(input("Presione '1' para reiniciar la calculadora: "))
      if (reiniciar == "1"):  
        clear()
        Calculadora()  

    elif (opcion == 5):
      clear()
      print("------------------------------------------------")
      print("----- RESULTADOS FINALES DE LA CALCULADORA -----")
      print("------------------------------------------------")
      print()
      print("1. Total de sumas realizadas: ",cont_suma)
      print("   Resultados = ",VECSUMA) 
      print()  
      print("2. Total de restas realizadas: ",cont_resta)
      print("   Resultados = ",VECRESTA) 
      print()  
      print("3. Total de multiplicaciones realizadas: ",cont_multi)
      print("   Resultados = ",VECMULTI) 
      print()  
      print("4. Total de divisiones realizadas: ",cont_divi)
      print("   Resultados = ",VECDIVI)
   

  elif (opcion == 5):
    print()
    print("   ALERTA: Debe realizar operaciones antes de salir")
    print()
    volver = str(input("Presione '1' para regresar al menú: "))
    while (volver != "1"):
      print()
      volver = str(input("Presione '1' para regresar al menú: "))
    if (volver == "1"):  
      clear()
      Calculadora() 

  else:
    print()
    print("   ALERTA: No seleccionaste una opcion correcta")
    print()
    volver = str(input("Presione '1' para regresar al menú: "))
    while (volver != "1"):
      print()
      volver = str(input("Presione '1' para regresar al menú: "))
    if (volver == "1"):  
      clear()
      Calculadora() 

import os
clear = lambda: os.system('clear')

VECSUMA = []
VECRESTA = []
VECMULTI = []
VECDIVI = []

Calculadora()