def inicPilha():
    lista = []
    return lista
def Pilhavazia(s):
    if len(s)==0:
        return "True"
    else: 
        return "False"
def PilhaCheia(s):
    if len(s)>0:
        return "True"
    else: 
        return "False"
def top(s):
    return s[len(s)-1] 
def pop(x):
    return x.pop()
def push(z, txt):
    z.append(txt)
 