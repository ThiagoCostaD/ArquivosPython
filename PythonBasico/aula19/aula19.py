#       Índice
#       0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nstring = ' '
letraM = input('Qual letra deseja colocar maiúscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == letraM:
        nstring += letraM.upper()
    else:
        nstring += letra
    contador +=1

print(nstring)
