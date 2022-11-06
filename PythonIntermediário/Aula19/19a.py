with open('abcd.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.write('Linha 4\n')
    
    file.seek(0)
    print(file.read)