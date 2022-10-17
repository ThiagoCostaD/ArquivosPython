cpf = 08868830671
novo_cpf = cpf[:-2]

reverso = 10
for index in range (19):
    if index > 8:
        index -= 9
        print(index)


        reverso -= 1
        if reverso < 2:
            reverso = 11