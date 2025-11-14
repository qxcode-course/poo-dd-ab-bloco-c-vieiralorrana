class Cliente:
    def __init__(self, id: str, telefone: int):
        self.__id = id
        self.__telefone = telefone
    
    def getPhone(self):
        return self.__id
    
    def setPhone(self, telefone: int):
        self.__telefone = telefone
    
    def getId(self):
        return self.__id
    
    def setId(self, id: str):
        self.__id = id
    
    def __str__(self):
        return f"{self.getId()}:{self.getPhone()}"

class Cinema:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        
    

