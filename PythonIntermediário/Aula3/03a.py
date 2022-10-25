def func(*args):
    args = list(args)
    args[0] = 77
    print(args)

func(1,2,22,54,65,7,6)

print('================================================================')

def func(*args):
    for v in args:
        print(v)

func(1,2,22,54,65,7,6)
