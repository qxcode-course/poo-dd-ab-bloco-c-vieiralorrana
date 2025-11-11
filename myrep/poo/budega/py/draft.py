class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f"{self.getNome()}"

class Mercantil:
    def __init__(self, quantidade_caixas: int):
        self.caixas: list[Cliente | None] = []
        self.quantidade_caixas = quantidade_caixas
        for _ in range(quantidade_caixas):
            self.caixas.append(None)
        self.fila: list[Cliente] = []

    def arrive(self, cliente: Cliente):
        self.fila.append(cliente)
    
    def call(self, index: int):
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.fila) == 0:
            print("fail: sem clientes")
            return
        self.caixas[index] = self.fila[0]
        del self.fila[0]
    
    def finish(self, index: int):
        if index < 0 or index > self.quantidade_caixas-1:
            print("fail: caixa inexistente")
            return
        
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return
        
        aux = self.caixas[index]
        self.caixas[index] = None
        return aux
    
    def __str__(self):
        caixas = ", ".join(["-----" if x is None else str(x) for x in self.caixas])
        saida: str = f"Caixas: [{caixas}]\n"
        fila = ", ".join([str(x) for x in self.fila])
        saida += f"Espera: [{fila}]"
        return saida
    
def main():
    mercantil = Mercantil(0)
    cliente = Cliente("")

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(mercantil)
        elif args[0] == "init":
            quantidade_caixas = int(args[1])
            mercantil = Mercantil(quantidade_caixas)
        elif args[0] == "arrive":
            nome = args[1]
            cliente = Cliente(nome)
            mercantil.arrive(cliente)
        elif args[0] == "call":
            index = int(args[1])
            mercantil.call(index)
        elif args[0] == "finish":
            index = int(args[1])
            mercantil.finish(index)


main()