class Estudante(Pessoa):
     def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    

