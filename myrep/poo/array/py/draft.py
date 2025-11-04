vazio: list[int] = []

class Foo:
    def __init__(self, nome: str):
        self.nome = nome

lista_foo: list[Foo] = ["Sapo", "Pato", "Gato"]
lista_foo.append("Rato")
lista_foo.insert(0, "Canguru")
lista_foo.pop()
lista_foo.pop(0)
lista_foo.insert(2, "Castor")
lista_foo.pop(1)
# print("lorrana".join(lista_foo)) 

numeros = list(range(21))
import random
outros_numeros = [random.randint(0, 99) for _ in range(10)]
print(numeros)

# for numeros in numeros:
    # print(numeros)

# for i in range(len(numeros)):
    # print(i, numeros[i])

# if 50 in numeros:
    # print("tem 5")
# else:
    # print("AAAAAAAAAAAAAAAAAAAAAAAA")

# busca = 5
# for numeros in numeros:
#    if numeros == busca:
    #    print("Simmm")
    #    break
#    else:
    #    print("Nao....")

pares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    
# print(pares)

impares = []
for i in numeros:
    if i % 2 != 0:
        impares.append(i)
    
# print(impares)

# for i in numeros:
#    print(i ** 2)

for i in numeros:
    if i == 3:
        numeros.pop(i)

# print(numeros)

