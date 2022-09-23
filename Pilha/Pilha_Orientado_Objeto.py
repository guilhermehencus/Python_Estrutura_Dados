""" 

            implementação de funções básicas para pilha

"""
class Pilha:



    def __init__(self, pilha):
        self.pilha = pilha

    def Pilhavazia(self):
        if len(self.pilha) > 0:
            print("Pilha Cheia")
            return False
        else:
            print("Pilha Vazia")
            return True

    def PilhaCheia(self):
        if len(self.pilha) > 0:
            print("Pilha Cheia")
            return True
        else:
            print("Pilha Vazia")
            return False
    def top(self):
        return print(self.pilha[len(self.pilha) - 1])                       
    def push(self,elemento):
        self.pilha.append(elemento)
    def pop(self):
        return print(self.pilha.pop())
        #return primeiro
lista = Pilha ([])
# true
lista.Pilhavazia()
lista = Pilha (["a", "b", "c"])
# true
lista.PilhaCheia()
# c no topo
lista.top()
# inserir o 'd'
lista.push("d")
# d no topo
lista.top()
# remover o 'd'
lista.pop()
# c de novo no topo
lista.top()