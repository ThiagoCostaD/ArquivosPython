d1 = {
    'str' : 'valor',
    123: 'valor1',
    (1,2,3,4,5) : 'Tupla',
}
d1['naotem'] = 'agora tem.'
if 'naotem' in d1:
    print(d1['naotem'])

print(d1[(1,2,3,4,5)])
print('\n')

print('===================================\n')

d1 = {
    'str' : 'valor',
    123: 'valor1',
    (1,2,3,4,5) : 'Tupla',
}
d1['nome da chave'] = 'Jesus é o caminho'
if d1.get('nome da chave') is not None:
    print(d1.get('nome da chave'))

print('123321')
print('\n')

print('===================================\n')

d1 = {
    'str' : 'valor',
    123: 'valor1',
    (1,2,3,4,5) : 'Tupla',
}

del d1['str']

print(d1)
print('\n')

print('===================================\n')

d1 = {
    'str' : 'valor',
    123: 'valor1',
    (1,2,3,4,5) : 'Tupla',
}
print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())
