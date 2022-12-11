class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está Filmando!')
            return

        print(f'{self.nome} está Filmando!')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está filmando!')
            return
        print(f'{self.nome} parou de filmar!')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando!')
            return
        print(f'{self.nome} está fotografando...')


c1 = Camera('Cannon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
# print(c1.filmando)
# print(c2.filmando)
