while True:
    print()
    n1 = input('Digite o número: ')
    n2 = input('Digite o número: ')
    operador = input('Digite o operador:')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not n1.isnumeric() or not n2.isnumeric():
        print("Você precisa digitar um número")
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 / n1)
    else:
        print('Operador invalido')
