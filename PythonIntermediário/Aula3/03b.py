def func(*args):
    print(args)

lista = [1,2,22,54,65,7,6]
func(*lista, 10, 20, 30, 40)

print('================================================================')

def func(*args):
    print(args)

lista = [1,2,22,54,65,7,6]
lista2 = [10, 20, 30, 40]
func(*lista, *lista2)

print('================================================================')

def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

lista = [1,2,22,54,65,7,6]
lista2 = [10, 20, 30, 40]
func(*lista, *lista2, nome='Thiago', sobrenome='Costa')
