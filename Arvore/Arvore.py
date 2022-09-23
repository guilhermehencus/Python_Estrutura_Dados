"""----------------------------------------------------------------------------------------
                    
                    IMPLEMENTANDO UMA CLASSE PARA A ÁRVORE BINÁRIA
                    
----------------------------------------------------------------------------------------"""


class Tree:
    def __init__(self, val=None, left=None, right=None):
        if val != None:
            self.val = val
        else:
            self.val = None
        if left != None:
            self.left = left
        else:
            self.left = None
        if right != None:
            self.right = right
        else:
            self.right = None
# MÉTODO PARA INSERÇÃO DE NOVOS NÓS

    def insert(self, val):

        if self.val:                    # TESTO SE O NÓ JÁ TEM VALOR, SE SIM, DESCEMOS PARA INSERIR À ESQUERDA OU DIREITIA

            # SE O NOVO VALOR É MENOR DO QUE O VALOR DO NÓ, INSERE À ESQUERDA.
            if val < self.val:
                if self.left is None:   # SE NÃO HOUVER UM VALOR À ESQUERDA, INSERE CRIANDO UM NOVO NÓ, COM O VALOR A
                    # A SER INSERIDO SENDO O PRÓPRIO VALOR DO NÓ
                    self.left = Tree(val)
                else:                 
                    # CASO JÁ EXISTA UM VALOR À ESQUERDA, CHAMA A FUNÇÃO INSERT RECURSIVAMENTE
                    # PARA PROCEDER A INSERÇÃO DESTE ELEMENTO, POIS DEVEM SER FEITAS
                    # ANÁLISES DE EM QUAL POSIÇÃO ESTE VALOR DEVE SER INSERIDO COM RELAÇÃO
                    # AO ELEMENTO À ESQUERDA AO QUAL ELE ESTÁ SUBORDINADO.
                    self.left.insert(val)
            else:
                if self.right is None:  # O MESMO CONCEITO QUE SE APLICOU À ESQUERDA, SE APLICA À DIREITA.
                    self.right = Tree(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val              
            # SE NÃO HOUVESSE VALOR NO NÓ RAIZ,
            # O NÓ RAIZ RECEBE O VALOR PASSADO PELA FUNÇÃO ISERT

    def print_tree(self):  # FUNÇÃO PARA PERCORRER A ÁRVORE E IMPRIMIR
        if self.left:               
            # SE EXISTIR ELEMENTO À ESQUERDA, CHAMAMA
            # RECURSIVAMENTE A PRÓPRIA FUNÇÃO, PARA IMPRIMIR O QUE
            # ESTIVER À ESQUERDA, E ASSIM POR DIANTE.
            self.left.print_tree()
        # FINALIZADOS OS ELEMENTOS À ESQUERDA, IMPRIMIMOS O NÓ RAIZ
        print(self.val)

        if self.right:              
            # SE HOUVER ELEMENTOS À DIREITA, CHAMA RECURSIVAMENTE
            # A FUNÇÃO IMPRIMINDO ESTES ELEMENTOS  ATÉ NÃO ENCONTRAR MAIS NADA.
            self.right.print_tree()

    def __repr__(self):             # DEFINIMOS FORMATO DE IMPRESSÃO DE UM OBJETO DA CLASSE TREE
        return ' %s <- %s -> %s ' % (self.left and self.left.val, self.val, self.right and self.right.val)


arvore = Tree(15)
print(arvore.val)
arvore.insert(10)
print(arvore)
arvore.insert(20)
print(arvore)
arvore.insert(11)
arvore.insert(18)
arvore.insert(25)
arvore.insert(29)
arvore.insert(22)
arvore.insert(6)
arvore.insert(3)
arvore.insert(2)
arvore.insert(7)
arvore.insert(5)
arvore.print_tree()
