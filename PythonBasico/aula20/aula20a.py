texto = 'Python'
nstring = ' '

for letra in texto:
    if letra == 't':
        nstring = nstring + letra.upper()
    elif letra =='h':
        nstring += letra.upper()
    else:
        nstring += letra

print(nstring)
