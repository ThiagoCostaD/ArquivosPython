def func1(*arg, **kwarg):
    print(arg)
    print(kwarg['nome'], kwarg['sobre'])


def func2():
    vari = 'Thiago'
    return vari

var = func2()
func1(var,nome= 'Thiago', sobre= 'Costa')