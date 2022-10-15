usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Thiago'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você esta logado')
else:
    print('Usuário ou senha inválido')