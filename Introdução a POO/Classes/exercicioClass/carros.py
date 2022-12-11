class Carro:
    def __init__(self, nome, ):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome, ):
        self.nome = nome


class Fabricante:
    def __init__(self, nome, ):
        self.nome = nome


ford = Fabricante('Ford')
motor1 = Motor('1.0')
motor2 = Motor('1.5')
motor3 = Motor('2.5')

ka = Carro('Ka')
ka.fabricante = ford
ka.motor = motor1

ecosport = Carro('Ecosport')
ecosport.fabricante = ford
ecosport.motor = motor2

ranger = Carro('Ranger')
ranger.fabricante = ford
ranger.motor = motor3

print(ka.motor, ka.fabricante.nome, ka.motor.nome)
print(ecosport.motor, ecosport.fabricante.nome, ecosport.motor.nome)
print(ranger.motor, ranger.fabricante.nome, ranger.motor.nome)
