secreto = 'te amo valeria'
digitadas = []
chances = 4
while True:
    if chances <= 0:
        print('Você perdeu!!!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("haha, isso não vale, Digite apenas uma letra.")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Acertou, a letra {letra} existe na palavra.')
    else:
        print(f'Errou, a letra {letra} Não existe na palavra.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
            print(f'Você ganhou!!!!!!!!! A palavra era {secreto_temporario} ')
            break
    else:
            print(f'A palavra secreta esta assim: {secreto_temporario}')
    if letra not in secreto:
        chances -=1
    print(f'Você ainda tem {chances}.\n')
