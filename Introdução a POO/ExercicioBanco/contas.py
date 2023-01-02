import abc


class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.valor += valor
        self.detalhes(f'(DEPÓSITO {valor}')

    def detalhes(self, msg=''):
        print(f'O seu saldo é{self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor}')
            return self.saldo

    print('Não foi possível sacar o valor desejado')
    self.detalhes(f'(SAQUE {valor}')


if __name__ == '__main__':
    ...
