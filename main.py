caminho_arquivo = 'C:\\Thiago\\ArquivosPython\\'
caminho_arquivo += 'aula23_5'

#arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('#########\n')
    arquivo.write('Linha2\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
