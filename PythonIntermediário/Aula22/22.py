lista = [0]
dicionario = {0}
conjunto = set()
tupla = (0)
string = '0'
inteiro = 1
flutuante = 6.0
nada = None
falso = False
intervalo = range(6)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy('lista'))
print(f'{dicionario=}', falsy('dicionario'))
print(f'{conjunto=}', falsy('conjunto'))
print(f'{tupla=}', falsy('tupla'))
print(f'{string=}', falsy('string'))
print(f'{inteiro=}', falsy('inteiro'))
print(f'{flutuante=}', falsy('flutuante'))
print(f'{nada=}', falsy('nada'))
print(f'{falso=}', falsy('falso'))
print(f'{intervalo=}', falsy('intervalo'))
