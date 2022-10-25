lista = [
    ['P1', 7],
    ['P2', 22],
    ['P3', 5],
    ['P4', 60],
    ['P5', 95],
]

def func(item):
    return item[1]

lista.sort(key=func, reverse=True)
print(lista)

print('======================================================================\n')

lista = [
    ['P1', 7],
    ['P2', 22],
    ['P3', 5],
    ['P4', 60],
    ['P5', 95],
]

lista.sort(key=lambda item: item [1], reverse=False)
print(lista)

print('======================================================================\n')

lista = [
    ['P1', 7],
    ['P2', 22],
    ['P3', 5],
    ['P4', 60],
    ['P5', 95],
]

print(sorted(lista, key=lambda i: i[0], reverse=True))
print(lista )
