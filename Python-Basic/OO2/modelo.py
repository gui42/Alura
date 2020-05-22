class Programa:
    def __init__(self, nome, ano_lancamento):
        self._nome = nome
        self.ano_lancamento = ano_lancamento
        self._likes = 0

    def get_likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f"Nome: {self._nome} ano: {self.ano_lancamento}, likes: {self._likes}"


class Filme(Programa):

    def __init__(self,nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def get_duracao(self):
        return self.duracao

    def print_nome(self):
        print(self._nome)

    # transforma em str, pra função print
    def __str__(self):
        return f"{self._nome.title()}\n\tAno: {self.ano_lancamento}\t Duracao:{self.duracao}\t Likes: {self._likes}"


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def get_temporadas(self):
        return self.temporadas

    def __str__(self):
        return f"{self._nome.title()}\n\tAno: {self.ano_lancamento}\t Temporadas: {self.temporadas}\tLikes: {self._likes}"


class Playlist():

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def tamanho(self):
        return len(self._programas)

    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas //só pra lembrar que isso existe
