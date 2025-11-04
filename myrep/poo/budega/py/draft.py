class Cliente:
    def __init__(self, nome: str):
        self.__nome: str = nome
    
    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f"{self.getNome()}"
    
class Mercantil:
    caixa: list[Cliente] = []