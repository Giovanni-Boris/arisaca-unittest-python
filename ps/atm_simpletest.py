import os
cuentas={'001' : 'Dave' , '123': 'Luna' , '456': 'Joel', '765': 'Jack' , '341': 'Danitza'}
import unittest
class Cajero:

    def __init__(self):
        self.continuar = True
        self.monto = 5000


    def contraseña(self):
        print(cuentas)
        contador = 1
        while contador <= 3:
            x = input("ingrese su contraseña:" )
            user = cuentas.get(x)
            if user!=None:
                print("Contraseña Correcta")
                print(f"Bienvenido {user}")
                break
            else:
                print(f"Contraseña Incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("No puede realizar operaciones.")
                    self.continuar = False
                contador+=1

    def menu(self):
        os.system("cls")   #esto es solo para windows
        self.contraseña()
        if self.continuar == False:
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
                    self.depositar()
                elif opcion == "2" :
                    self.retiro()
                elif opcion == "3":
                    self.ver()
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

    def depositar(self):    
	    dep = int(input("Ingrese su monto a depositar:"))
	    print(self.validarDepositar(dep))
            
    # Funcion para validar monto a depositar
    def validarDepositar(self,dep):
        if dep <= 0:
            return "Monto no valido"
        if dep>3000:
            return "Monto no valido para menos de 3000 soles"
        self.monto+=dep
        return f"Su nuevo saldo es {self.monto}"

 

    def retiro(self):
        retirar=int(input("¿Cuánto desea retirar? : "))
        print("Su monto actual es", self.monto)
        print(self.validarRetiro(retirar))
        

    def validarRetiro(self,retirar):
        if retirar > 3000:
            return "Monto no permitido de retirar > 3000 soles"
        elif retirar <=0:
            return "Monto no valido"
        elif self.monto >= retirar :
            self.monto-=retirar
            return f"Retiro exitoso nuevo monto es {self.monto}"
        else:
            return "Imposible de realizar, su monto es menor"


    def ver(self):
        print("Su saldo es: " , self.monto)

 

#app = Cajero()

class TestCajeroDepositarRetirar(unittest.TestCase):
    def test_ValidarCuentas(self):
        app = Cajero()
        app.contraseña
        self.assertEqual(cuentas.get("123") ,"Luna")
        self.assertEqual(cuentas.get("456") , "Joel")
        self.assertTrue(cuentas.get("1212e") == None)
        
        
    def test_DepositaMayor3000(self):
        app = Cajero()
        self.assertEqual(app.validarDepositar(3001), "Monto no valido para menos de 3000 soles")

    def test_DepositaRetirar3000(self):
        app = Cajero()
        self.assertTrue(app.validarRetiro(3001) == "Monto no permitido de retirar > 3000 soles")

    def test_DepositaRetirarMasDelMonto(self):
        app = Cajero()
        #Monto 5000
        app.validarRetiro(2000)
        self.assertTrue(app.monto == 3000)
        app.validarRetiro(2000)
        self.assertTrue(app.monto == 1000)
        app.validarRetiro(1001)
        self.assertFalse(app.monto == -1)

    def test_DepositaRetirarNoNegativos(self):
        app = Cajero()
        #Monto 5000
        app.validarRetiro(-5000)
        self.assertTrue(app.monto == 5000)
        app.validarDepositar(-2000)
        self.assertTrue(app.monto == 5000)
        app.validarRetiro(-5000)
        self.assertFalse(app.monto == 0)
        

if __name__ == '__main__':
    unittest.main()