file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.write('Linha 4\n')

file.seek(0, 0)
print('lendo linhas: ')
print(file.read())
print('#' * 30)
print()

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.close()