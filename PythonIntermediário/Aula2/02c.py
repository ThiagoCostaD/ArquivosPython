def fb(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FIZZBUZZ'
    if numero % 5 == 0:
        return 'BUZZ'
    if numero % 3 == 0:
        return 'FIZZ'
    return numero

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
