class Pessoa:
    
    def __init__(self, nome:str, idade: int):
        self._nome: str = nome
        self._idade: int = idade

    @property
    def nome(self) -> str:
       
        return self._nome