print('Esculha uma opção')

perguntas = {
    'pergunta 1':{
        'pergunta': 'quanto é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',       
    },
    'pergunta 2':{
        'pergunta': 'quanto é 4+4?',
        'respostas': {'a': '3', 'b': '8', 'c': '5',},
        'resposta_certa': 'b',       
    },
}
print()

resposta_certa = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Alternativas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Qual a sua escolha: ")
    
    if resposta_usuario == pv['resposta_certa']:
        print('Acertou')
        resposta_certa += 1
    else:
        print('Errou')
    
    print()

qtd_pergutans = len(perguntas)
porcentagem_acertos = resposta_certa / qtd_pergutans * 100

print(f'você acertou {resposta_certa} pergunta(s).')
print(f'Sua porcentagem de acerto foi de {porcentagem_acertos}%')
