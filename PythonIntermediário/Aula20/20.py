def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_cliente1 = ['Thiago']
clientes1 = lista_de_clientes(['João', 'José', 'Maria'], lista_cliente1)
clientes2 = lista_de_clientes(['Paulo', 'Pedro'])
clientes3 = lista_de_clientes(['Ronaldo'])

print(clientes1)
print(clientes2)
print(clientes3)
