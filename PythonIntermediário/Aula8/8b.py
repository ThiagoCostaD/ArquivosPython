d1 = {
    'str' : 'valor',
    123: 'valor1',
    (1,2,3,4,5) : 'Tupla',
}
print(len(d1))
print('\n')

print('===================================\n')

d1 = {
    'chave1' : 'valor',
    'chave2' : 'valor1',
    'chave3' : 'Tupla',
}

for k in d1.items():
    print(k)
print('\n')

print('===================================\n')

d1 = {
    'chave1' : 'valor',
    'chave2' : 'valor1',
    'chave3' : 'Tupla',
}

for k in d1.items():
    print(k[0], k[1])
print('\n')

print('===================================\n')

d1 = {
    'chave1' : 'valor',
    'chave2' : 'valor1',
    'chave3' : 'Tupla',
}

for k, v in d1.items():
    print(k, v)
