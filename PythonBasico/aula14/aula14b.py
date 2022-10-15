nome = input('digite seu primeiro nome: ')

qtd_caracteres = len(nome)

if qtd_caracteres < 4:
    print('seu nome é curto')
elif 5 <= qtd_caracteres <= 6:
    print('seu nome é normal')
elif qtd_caracteres > 6:
    print('Seu nome é muito grande')