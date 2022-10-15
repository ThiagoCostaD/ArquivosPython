"""
manioulando strings
* string indice
* fatiamento de strings [inicio:fim:passo]
*Funções built-in len, abs, typy, print, etc...
essas funções podem ser usadas diretamente em cada tipo.
"""

texto = 'Python_s2'
print(texto[0], texto[2], texto[4], texto[6], texto[8])

url = 'www.google.com/'
print(url[:-1])

nova_string = texto[2:6]
nova_string1 = texto[:6]
nova_string2 = texto[7:]
nova_string3 = texto[0::2]
print(nova_string)
print(nova_string1)
print(nova_string2)
print(nova_string3)
