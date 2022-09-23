class NodoLista:

    """Esta classe representa um nodo de uma lista encadeada."""

    def __init__(self, dado=0, proximo=None):
        self.dado = dado
        self.proximo = proximo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class ListaEncadeada:

    """Esta classe representa uma lista encadeada."""

    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    # Inserção de um novo nodo no início da lista Encadeada.

    def insere_no_inicio(self, novo_dado):
        # 1) Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = NodoLista(novo_dado)
        # 2) Faz com que o novo nodo seja a cabeça da lista.
        novo_nodo.proximo = self.cabeca
        # 3) Faz com que a cabeça da lista referencie o novo nodo.
        self.cabeca = novo_nodo

    # Inserção de elemento no meio do nodo:
    def insere_depois(self, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista. Se não existe, use o método insere_no_inicio."
        # Cria um novo nodo com o dado desejado.
        novo_nodo = NodoLista(novo_dado)
        # Faz o próximo do novo nodo ser o próximo do nodo anterior.
        novo_nodo.proximo = nodo_anterior.proximo
        # Faz com que o novo nodo seja o próximo do nodo anterior.
        nodo_anterior.proximo = novo_nodo

    def busca(self, valor):
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        if corrente == None:
            return "O elemento " + str(valor) + " não existe"
        else:
            return corrente

    def remove(self, valor):
        assert self.cabeca, "Impossível remover valor de lista vazia."
        # Nodo a ser removido é a cabeça da lista.
        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            # Encontra a posição do elemento a ser removido.
            anterior = None
            corrente = self.cabeca
            while corrente and corrente.dado != valor:
                anterior = corrente
                corrente = corrente.proximo
            # O nodo corrente é o nodo a ser removido.
            if corrente:
                anterior.proximo = corrente.proximo
            else:
                # O nodo corrente é a cauda da lista.
                anterior.proximo = None


# Testando a inserção de um elemento na lista encadeada criada:

lista = ListaEncadeada()
print("Resultado:", lista.busca(1))
print("Lista vazia:", lista)
lista.insere_no_inicio(5)
print("Lista após inserção :", lista)
lista.insere_no_inicio(10)
print(lista)
lista.insere_no_inicio(1)
lista.insere_no_inicio(7)
lista.insere_no_inicio("valor")

print("Lista após  nova inserção :", lista)
lista.remove(10)
print("Lista após  remoção do 10 :", lista)

#nodo_anterior = lista.cabeca

"""
lista.insere_depois(nodo_anterior, 3)
print("Inserindo um novo elemento depois de um outro:", lista)
### Ou então...
print("cabeca da lista: " + str(lista.cabeca))

lista.insere_depois(lista.cabeca, 4)
print("Inserindo quarto novo elemento depois de um outro:", lista)

### carregando vários elementos na lista

for i in range(8):
    lista.insere_no_inicio(i)
    print("Lista:", lista)

for i in range(8, -4, -2):
    elemento = lista.busca(i)
    if elemento:
        print("Elemento {0} presente na lista!".format(i))
    else:
        print("Elemento {0} não encontrado.".format(i))

for i in range(5):
    lista.insere_no_inicio(i)
print("Lista:", lista)

print("Removendo elementos:")
for i in range(5):
    lista.remove(i)
    print("Removendo o elemento {0}: {1}".format(i, lista))
"""
