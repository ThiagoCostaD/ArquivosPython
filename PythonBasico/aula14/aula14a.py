hora = input('qual é a hora agora? ')
min = int(input('qual é os minutos? '))
hora = int(hora)

if 00 <= hora <= 11 and 00 <= min <= 59:
    print("bom dia")
elif 12 <= hora <= 17 and 00 <= min <= 59:
    print('boa tarde')
elif 18 <= hora <= 23 and 00 <= min <= 59:
    print('boa noite')
else:
    print('hora errada')