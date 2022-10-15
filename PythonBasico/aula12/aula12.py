usuario = input('Digite seu usuário:')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Quantidade inválida, minimo 6 caracteres')
else:
    print('Você foi cadastrado no sistema')
