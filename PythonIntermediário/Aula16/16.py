"""
    Zip - unindo iteráveis
    Zip_longest - itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', "Belo Horizonte", 'Manaus', 'Rio de Janeiro']
estados = ['SP', 'MG', "AM"]

cidade_estado = zip(
    indice,
    estados,
    cidades,
    )

for indice, estados, cidades in cidade_estado:
    print(indice, estados, cidades)
