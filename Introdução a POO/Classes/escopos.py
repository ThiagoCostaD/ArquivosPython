class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} esta comendo uma {alimento}'


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('zebra'))
