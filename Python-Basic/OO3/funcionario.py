class Funcionario:
    def __innit__(self, nome):
        self.nome = nome

    def registra_horas(self):
        print("Horas registradas")

    def mostrar_tarefas(self):
        print("Fez mt coisa")


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print("Fez mt coisa Caelumer")

    def busca_cursos_do_mes(self, mes = None):
        print(f"Mostrando cursos - {mes}" if mes else "Mostrando cursos desse mes")


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print("Fez mt coisa alurete")

    def busca_perguntas_sem_resposta(self):
        print("Buscando perguntas não respondidas no forum")

class Hipster:
    def __str__(self):
        return f"Hipster {self.nome}"

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass


        
