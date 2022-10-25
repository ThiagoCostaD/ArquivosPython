clientes = {
    'cliente1' : {
        'nome' : "Thiago",
        'sobrenome' : 'Costa',
    },
    'cliente2' : {
        'nome' : "Valéria",
        'sobrenome' : 'Costa',
    },
    'cliente3': {
        'nome': "Valentina",
        'sobrenome': 'Costa',
    },
    'cliente4': {
        'nome': "Luíza",
        'sobrenome': 'Costa',
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dadosK, dadosV in clientes_v.items():
        print(f'\t{dadosK} = {dadosV}')
    print('\n')