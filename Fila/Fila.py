def inicFila():
    fila = []
    return fila


def Filavazia(q):
    if len(q) == 0:
        return "True"


def Filacheia(q):
    if len(q) > 0:
        return "True"


def Enqueue(q, x):
    q.append(x)


def Dequeue(q):
    return q.pop(0)
