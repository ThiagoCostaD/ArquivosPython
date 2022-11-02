carrinho =  []

carrinho.append(('Produto 1', 35))
carrinho.append(('Produto 2', 15))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 60))

total = 0

valor_carrinho = [produto[1] + total for produto in carrinho]
print(sum(valor_carrinho))
