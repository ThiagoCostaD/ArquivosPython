"""
formatando valores com modificadores

:s - texto (strings)
:d - inteiros (int)
:f - números de pontos flutuantes (float)
:.(NÚMERO)f - quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ⁾(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^- centro
"""
num1 = 1150
num2 = 3
divisao = num1/num2
nome = 'thiago'

print( '{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print(f'{nome:s}')
print(f'{num1:0<10}')
print(f'{num1:0>10}')
print(f'{num1:0^10}')
print(f'{num1:.2f}')
print(f'{num1:0>10.2f}')
nome_formatado = '{:@>10}'.format(nome)
print(nome_formatado)
print(nome.lower())
print(nome.upper())
print(nome.title())


