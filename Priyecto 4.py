class CuentaBancaria:
    
    def __init__(self, saldo):
        
        self.saldo = saldo
        
    def Retirar(self, cantidad): 
        
        if cantidad <= self.saldo:
            
            self.saldo -= cantidad
            
            print("Se han retirado" , cantidad, "de tu cuenta. Saldo actual: ", self.saldo)
        else:
            print("No teiens saldo suficiente para realizar un retiro")
    def Depositar(self, deposito):
        
        self.saldo += deposito
        
        print("Se han depositado" , deposito , "en tu cuenta. Saldo actual: ", self.saldo)
    def Consultar_saldo(self):
        
     print("Tu saldo actual es: ", self.saldo)
           
import os

import time


cuenta = CuentaBancaria(0)

option = 0

while option != 4:
    
 print("\n--- Menú ---")
 print("1. Depositar")
 print("2. Retirar")
 print("3. Consultar saldo")
 print("4. Salir")
    
 option = int(input("Seleccione una opción: "))
 
 time.sleep(1.5)
 os.system("cls")

 if option == 1:
     
    deposito = float(input("Ingrese la cantidad a depositar: "))
    
    cuenta.Depositar(deposito)
    
    time.sleep(2.5)
    os.system("cls")
    
 elif option == 2:
    
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    
    cuenta.Retirar(cantidad) 
      
    time.sleep(2.5)
    os.system("cls")
    
 elif option == 3:
    
    cuenta.Consultar_saldo()
    
    time.sleep(2.5)
    os.system("cls")
    
 elif option >4:
     
    print("Opción invalida. Elija una opción del 1 al 4")
    
    time.sleep(1.5)
 os.system("cls")
 
else:
    
    print("Que tenga lindo día")   