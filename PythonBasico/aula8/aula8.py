nome = 'Thiago Costa'
idade = 33
altura = 1.85
peso = 110
ano_atual = 2022
ano_nascimento = ano_atual - idade 
imc = peso/(altura**2)

print(f'O {nome} tem {idade} anos de vida')
print(f'Sua altura é {altura}, ele nasceu em {ano_nascimento}')
print(f'E seu IMC é {imc:.2f}')
