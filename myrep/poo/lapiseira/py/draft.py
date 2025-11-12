class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre 
        self.dureza = dureza
        self.tamanho = tamanho 
    
    def usoPorFolha(self):
        if self.dureza == "HB":
            return 1
        if self.dureza == "2B":
            return 2
        if self.dureza == "4B":
            return 4
        if self.dureza == "6B": 
            return 6
    
    def __str__(self):
        return f"[{self.calibre:.1f}:{self.dureza}:{self.tamanho}]"
    

class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre 
        self.bico: Grafite | None = None
        self.tambor: list[Grafite] = []
    
    def inserir(self, grafite: Grafite):
        if grafite.calibre != self.calibre:
            print("fail: calibre incompativel")
        else:
            self.tambor.append(grafite)
    
    def puxar(self):
        if self.bico is not None:
            print("fail: ja existe grafite")
        else:
            self.bico = self.tambor[0]
            del self.tambor[0]
        
    def escrever(self):
        if self.bico is None:
            print("fail: nao tem grafite")
            return
        
        if self.bico.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return
        
        uso = self.bico.usoPorFolha()
        tamanhoFinal = self.bico.tamanho - uso

        if tamanhoFinal < 10:
            print("fail: folha incompleta")
            return
        
        self.bico.tamanho(tamanhoFinal)
    
    def __str__(self):
        bico = "" if self.bico is None else self.bico
        tambor = "".join([str(x) for x in self.tambor])
        return f"calibre: {self.calibre:.1f}, bico: [{bico}], tambor: <{tambor}>"
    