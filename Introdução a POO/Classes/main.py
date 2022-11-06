from pessoa import Pessoa

p1 = Pessoa('Thiago', 33)
p2 = Pessoa('Luiz', 29)

p1.comer('manga')
p1.parar_comer()
p1.parar_comer()
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())