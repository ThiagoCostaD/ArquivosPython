import copy

d1 = {1:'a', 2:'b', 3:'c', 'd':['Thiago', 'valéria']}
v = copy.deepcopy(d1)

v[1] = 'Thiago'
v['d'][0] = 'Valentina'

print(d1)
print(v)
print('\n')
print('=======================================================')
print('\n')

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]
d1 = dict(lista)
print(d1)
