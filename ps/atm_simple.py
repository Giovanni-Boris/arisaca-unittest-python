# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:46:29 2023

@author: LAB02
"""
import os
from dataBase import cuentas

class Cajero:
    def __init__(self):
        self.continuar = True

    def contraseña(self, contraseñas):
        contador = 3
        if(contraseñas):
            contador = min(len(contraseñas), 3)
        usuario = None
        i = 0

        while contador > 0:
            if(not contraseñas):
                x = input("ingrese su contraseña:" )
            else:
                x = contraseñas[i]
            usuario = cuentas.get(x)

            if usuario != None:
                print("Contraseña Correcta")
                print(f"Bienvenido {usuario[0]}")
                break
            else:
                contador -= 1
                i += 1
                print(f"Contraseña Incorrecta, le quedan {contador} intentos")

        if(usuario):
            return [x, usuario[0]]
        else:
            return [x, usuario]

    def menu(self):
        #os.system("cls")
        contraseña, usuario = self.contraseña([])
        if not usuario:
            print("No puede realizar operaciones")
            return

        opcion = 0
        while opcion != "4":
            #os.system("cls")
            print(""" Bienvenido al cajero automatico
            ******Menú******
            1-  Depositar
            2- Retirar
            3- Ver saldo
            4- Salir """)
            opcion = input("Su opción es: ")
            if self.continuar:
                if opcion == "1" :
                    self.depositar(contraseña)
                elif opcion == "2" :
                    self.retiro(contraseña)
                elif opcion == "3":
                    self.ver(contraseña)
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("NO existe esa opción")
            else:
                if opcion in "123":
                    print("Imposible realizar esa operación")
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("No existe esa opción")

    def depositar(self, contraseña):
        dep = int(input("Ingrese su monto a depositar:"))
        print(self.validarDepositar(dep, contraseña))

    # Funcion para validar monto a depositar
    def validarDepositar(self, dep, contraseña):
        if dep <= 0:
            return "Monto no valido"
        if dep>3000:
            return "Monto no valido para menos de 3000 soles"
        cuentas.get(contraseña)[1] += dep
        #self.monto+=dep
        return f"Su nuevo saldo es {cuentas.get(contraseña)[1]}"

    def retiro(self, contraseña):
        retirar=int(input("¿Cuánto desea retirar? : "))
        print("Su monto actual es", cuentas.get(contraseña)[1])
        print(self.validarRetiro(retirar, contraseña))

    def validarRetiro(self, retirar, contraseña):
        if retirar > 3000:
            return "Monto no permitido de retirar > 3000 soles"
        elif retirar <=0:
            return "Monto no valido"
        elif cuentas.get(contraseña)[1] >= retirar :
            cuentas.get(contraseña)[1] -= retirar
            return f"Retiro exitoso nuevo monto es {cuentas.get(contraseña)[1]}"
        else:
            return "Imposible de realizar, su monto es menor"

    def ver(self, contraseña):
        print(f"Su saldo es: {cuentas.get(contraseña)[1]}")

#app = Cajero()
#app.menu()
