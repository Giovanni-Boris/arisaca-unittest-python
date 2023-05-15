import unittest
from atm_simple import Cajero
from dataBase import cuentas, salida

# testing
class testLogueoCuenta(unittest.TestCase):
    def test_validarMenosDeTresIntentos(self):
        cajero = Cajero()
        resultado = cajero.contraseña(['000', '099', '923', '777'])[1]
        self.assertEqual(resultado, None)

    def test_validarLogueoEnSegundoIntento(self):
        cajero = Cajero()
        # usuario Jack
        resultado = cajero.contraseña(['000', '666'])[1]
        self.assertEqual(resultado, 'Jack')

    def test_validarLogueoEnTercerIntento(self):
        cajero = Cajero()
        # usuario Jack
        resultado = cajero.contraseña(['000', '142', '123'])[1]
        self.assertEqual(resultado, 'Luna')

class TestCajeroDepositarRetirar(unittest.TestCase):
    def test_DepositaMayor3000(self):
        app = Cajero()
        self.assertEqual(salida.get(app.validarDepositar(3001, '001')), 1)

    def test_DepositaRetirar3000(self):
        app = Cajero()
        self.assertEqual(salida.get(app.validarRetiro(3001, '001')), 2)

    def test_DepositaRetirarMasDelMonto(self):
        app = Cajero()
        #Monto jack: 5500
        contraseña = '666'
        saldo = cuentas.get(contraseña)[1]

        app.validarRetiro(2000, contraseña)
        self.assertTrue(cuentas.get(contraseña)[1] == saldo - 2000)
        saldo -= 2000

        app.validarRetiro(2000, contraseña)
        self.assertTrue(cuentas.get(contraseña)[1] == saldo - 2000)
        saldo -= 2000

        self.assertEqual(salida.get(app.validarRetiro(1501, contraseña)), 3)

    def test_DepositaRetirarNoNegativos(self):
        app = Cajero()
        #Monto Luna: 4000
        contraseña = '123'
        saldo = cuentas.get(contraseña)[1]

        app.validarRetiro(-5000, contraseña)
        self.assertEqual(cuentas.get(contraseña)[1], saldo)

if __name__ == '__main__':
        unittest.main()
