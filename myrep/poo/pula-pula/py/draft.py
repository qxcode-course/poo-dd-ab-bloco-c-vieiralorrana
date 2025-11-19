class Crianca:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}:{self.idade}"
    
class Pulapula:
    def __init__(self):
        self.pulando: list[Crianca] = []
        self.esperando: list[Crianca] = []
    
    def arrive(self, crianca: Crianca):
        self.esperando.append(crianca)
    
    def enter(self):
        crianca = self.esperando[0]
        self.pulando.append(crianca)
        del self.esperando[0]

    
    def leave(self):
        crianca = self.pulando.pop()
        self.esperando.insert(0, crianca)
    
    def remove(self, crianca: Crianca):
        if crianca not in self.pulando:
            print(f"{crianca.nome} nao esta no pula-pula")
            return
        else:
            self.pulando.remove(crianca)
    
    def __str__(self):
        espera = ", ".join("" if len(self.esperando) == 0 else str(x) for x in self.esperando)
        pulando = ", ".join("" if len(self.pulando) else str(x) for x in self.esperando)
        return f"[{espera}] => [{pulando}]"

def main():
    pulapula = Pulapula()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pulapula)
        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            crianca = Crianca(nome, idade)
            pulapula.arrive(crianca)
        elif args[0] == "enter":
            pulapula.enter()
        elif args[0] == "leave":
            pulapula.leave()
        elif args[0] == "remove":
            crianca = args[1]
            pulapula.remove(crianca)
main()

        