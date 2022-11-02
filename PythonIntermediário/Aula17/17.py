listaA = [1,2,3,4,5,6,7]
listaB = [1,2,3,4]
listaFinal = [x + y for x, y in zip(listaA, listaB)]

'''listaFinal = []
for i in range(len(listaB)):
    listaFinal.append(listaA[i] +listaB[i])


listaFinal = []
for i, _ in enumerate(listaB):
    listaFinal.append(listaA[i] + listaB[i])
'''

print(listaFinal)