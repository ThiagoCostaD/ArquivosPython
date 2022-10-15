nome = 'Thiago Costa'
idade = 33
altura = 1.85
e_maior = idade > 18
peso = 110
imc = peso/(altura**2)

print(nome, 'tem', idade, 'anos de idade e seu imc é:', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
