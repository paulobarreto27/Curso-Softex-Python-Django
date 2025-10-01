class Pessoa:
    
    def __init__(self, nome:str, idade: int):
        self._nome: str = nome

    @property
    def nome(self) -> str:
       
        return self._nome