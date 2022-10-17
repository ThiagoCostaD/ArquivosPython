string = 'O Brasil é o país do futebol, o Brasil é PENTA.'
lista1 = string.split(' ')
lista2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
        
print(f'A palavra que apareceu mais vezes é {palavra}({contagem}x)')
