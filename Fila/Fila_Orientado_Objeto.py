""" 

            implementação de funções para fila

"""


class Fila:

    def __init__(self, fila):
        self.fila = fila

    def filaVazia(self):
        if len(self.fila) > 0:
            print("Fila Cheia")
            return False
        else:
            print("Fila Vazia")
            return True

    def filaCheia(self):
        if len(self.fila) > 0:
            print("Fila Cheia")
            return True
        else:
            print("Fila Vazia")
            return False

    def enqueue(self, elemento):
        self.fila.append(elemento)

    def dequeue(self):
        return print(self.fila.pop(0))

        # return primeiro
lista = Fila(([1, 2, 3]))
lista.filaCheia()
lista.dequeue()
lista.dequeue()
lista.dequeue()
lista.filaVazia()
