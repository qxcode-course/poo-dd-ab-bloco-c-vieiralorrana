class Cliente:
    def __init__(self, nome: str):
        self.__nome: str = nome
    
    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f"{self.getNome()}"
    
class Mercantil:
    def __init__(self, quantidade_caixa: int):
        self.caixa: list[Cliente | None] = []
        for _ in range(quantidade_caixa):
            self.caixa.append(None)
        self.fila: list[Cliente] = []
    
    def __str__(self) -> str:
        pessoas = ", ".join([("-----" if x is None else str(x)) for x in self.caixa])  
        saida: str = f"Caixas: [{pessoas} ]\n" 
        esperando = ", ".join([str(x) for x in self.fila])
        saida += f"Espera: [{esperando}]" 
        return saida
    
    def arrive(self, cliente: Cliente):
        self.fila.append(cliente)

    def leave(self, index: int) -> Cliente | None:
        if index < 0 or index > len(self.caixa):
            print("Indice invalido")
            return
        if self.caixa[index] is None:
            print("Caixa vazio")
            return
        aux = self.caixa[index]
        self.caixa[index] = None 
        return aux
    
    def give_up(self, nome: str):
        for i, cliente in enumerate(self.fila):
            if cliente.getNome == nome:
                del self.fila[i]
                break
    
    def call(self, index: int):
        if index < 0 or index > len(self.caixa):
            print("Indice invalido")
            return
        if len(self.fila) == 0:
            print("Fila vazia")
            return
        if self.caixa[index] is not None:
            print("Caixa ocupado")
            return
        self.caixa[index] = self.fila[0]
        del self.fila[0]

mercantil = Mercantil(5)
mercantil.arrive(Cliente("Fulana"))
mercantil.arrive(Cliente("Ciclana"))
mercantil.arrive(Cliente("Beltrana"))
mercantil.call(3)
mercantil.call(0)
mercantil.arrive(Cliente("Louca da Silva"))
mercantil.arrive(Cliente("Elize Matsunaga"))
mercantil.leave(3)
mercantil.call(1)
mercantil.leave(0)
print(mercantil)