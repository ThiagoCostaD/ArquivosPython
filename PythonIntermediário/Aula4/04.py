variavel = 'valor'

def func():
    print(variavel)
def func2():
    global variavel
    variavel = 'Outro Valor'
    print(variavel)

func()
func2()

print(variavel)

print('==================================================================')

variavel = 'Novo valor'

def func():
    print(variavel)

def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg

func()
nova_variavel = func2(arg=variavel)

print(nova_variavel)

