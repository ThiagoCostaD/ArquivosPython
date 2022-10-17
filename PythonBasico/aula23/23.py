"""
Split, Join, Enumerate
*Split - dividir uma string
*Join -  juntar uma lista
*Enumerate - Enumerar elementos da lista
"""
string = 'o Brasil é o país do futebol, o Brasil é PENTA.'
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase')
