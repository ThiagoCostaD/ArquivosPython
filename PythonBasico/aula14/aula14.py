n1 = float(input("digite um número inteiro: "))
operacao = n1 % 2

if operacao == 0:
    print(f'Seu número {n1} é par.')
elif operacao == 1:
    print(f'Seu número {n1} é impar')
else:
    print(f'{n1} não é inteiro')