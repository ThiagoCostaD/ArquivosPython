string = '0123456789012345678901234567890123456789012345678901234567890123456789'
numero = 10
lista = [string[indice: indice + 10]for indice in range(0, len(string), numero)]
retorno = '.'.join(lista)
print(lista)
print(retorno)