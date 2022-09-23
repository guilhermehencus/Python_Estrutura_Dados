#  receba 10 números em uma lista e usando recursividade calcule a soma destes números.
def soma(x, n):
    if n == 0:
        return x[n]
    else:
        return x[n] + soma(x, n-1)


lista = []
x = 0
while x < 10:
    lista.append(int(input("informe o número ")))
    x = x+1
print(f"Soma: {soma(lista, len(lista)-1)} ")
# receba um número e o seu expoente, e usando recursividade calcule a potência do número elevado ao expoente


def potencia(x, n):
    if n == 1:
        return x
    else:
        return x * potencia(x, n-1)


num = int(input("Informe um número "))
exp = int(input("Qual o número que você quer elevar"))
print(f"Potência de {num} é: {potencia(num, exp)} ")
# Escreva uma função recursiva para inverter uma lista.


def inv_lista(n):
    if n == 0:
        return lista
    else:
        lista.insert((len(lista)-1)-n, lista[len(lista)-1])
        lista.pop(len(lista)-1)
        return inv_lista(n-1)


lista = []
x = 0
while x < 5:
    lista.append(input("Escreva algo na lista "))
    x = x+1
print(f"A lista original: {lista}")
print(f"A lista invertida: {inv_lista(len(lista) - 1)} ")
#  Escreva um programa em para inverter uma string usando recursão.
lista = []


def inv_string(n):
    if n == 0:
        lista.append(char[n])
        palavra_inv = ' '.join(lista)
        return palavra_inv
    else:
        lista.append(char[n])
        return inv_string(n-1)


char = input("Escreva uma palavra")
print(f"Palavra original: {char}")
print(f"A palavra invertida: {inv_string(len(char) - 1)} ")
# Escreve uma função recursiva que , dado um número, faça a contagem regressiva (impressa) deste número até 0, imprimindo  "LANÇAR FOGUETE!" ao chegar em zero.


def contagem(n):
    if n == 0:
        return "LANÇAR FOGUETE!"
    else:
        print(f"{n}")
        return contagem(n-1)


numero = int(input("Informe um número "))
print(f"{contagem(numero)}")
