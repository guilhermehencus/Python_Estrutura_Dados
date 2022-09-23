# Criar um programa que permita a entrada de um número inteiro e retorne o seu dobro, através de uma função.

def DobroNumero(numero):
    dobro = numero*2
    return dobro


valor1 = int(input("Digita um número inteiro: "))
resultado = DobroNumero(valor1)
print(f"O dobro de {valor1} é: {resultado}")
# Criar um programa que receba um número e a potência à qual queremos elevar este número, e retorne o resultado usando uma função que tenha laço de repetição


def PotenciacaoNumero(numero, potencia):
    for x in range(0, potencia+1, 1):
        resultado = numero**x
    return resultado


valor1 = int(input("Digita um número: "))
expoente = int(input("Digita um número que você quer  elevar: "))
resultado = PotenciacaoNumero(valor1, expoente)
print(f"O {valor1} elevado a {expoente} é: {resultado}")
# Criar um programa que receba 2 valores e calcule o produto através de uma função que retorna valores.


def ProdutoNumero(numero, numero2):
    produto = numero*numero2
    return produto


valor = int(input("Digita um número: "))
valor2 = int(input("Digita um outro número: "))
resultado = ProdutoNumero(valor, valor2)
print(f" {valor} * {valor2} é: {resultado}")
# Criar um programa que receba um grau e o converta para radianos através de uma função. Fórmula: radiano = grau * pi / 180


def ConverterRadiano(grau):
    radiano = (grau*3.14)/180
    return radiano


valorgrau = float(input("Digita um valor em grau(s): "))
resultado = ConverterRadiano(valorgrau)
print(f"O grau {valorgrau} em radiano é: {round(resultado, 3)}")
# Criar um programa que mostre qual o maior valor entre dois números, utilizando uma função que não retorna valores


def MaiorNumero(num, num2):
    if num > num2:
        print(f"O número {num} é maior que {num2}")
    else:
        print(f"O número {num2} é maior que {num}")


valor = int(input("Digita um número: "))
valor2 = int(input("Digita um outro número: "))
if valor != valor2:
    MaiorNumero(valor, valor2)
else:
    print(f"Números Iguais")
# Criar um programa que receba um número que corresponda a um mês do 1º trimestre e escreva o mês correspondente; caso o usuário digite o número fora do intervalo deverá aparecer “mês inválido”, mas utilizando uma função


def MesPritrimestre(num_mes):
    if num_mes == 1:
        print(f"Mês Janeiro")
    elif num_mes == 2:
        print(f"Mês Fevereiro")
    elif num_mes == 3:
        print(f"Mês Março")
    elif num_mes >= 4:
        print(f"Mês inválido")


mesnumber = int(input("Digita um  número de mês no 1º trimestre: "))
MesPritrimestre(mesnumber)
# Criar um programa que retorne o fatorial de um número, usando uma função que receba um valor e retorne o fatorial desse valor. Fatorial de 5 = 5 x 4 x 3 x 2 x 1 = 120


def FatorialNum(num):
    count = num
    acunum = num
    while (count > 1):
        count -= 1
        acunum = acunum*count
    return acunum


valor = int(input("Digita um  número: "))
resultado = FatorialNum(valor)
print(f"O fatorial de {valor} é: {resultado}")
# Criar um programa que verifique se um número é primo ou não, através de uma função. Número primo é divisível somente por 1 e por ele mesmo


def NumeroPrimo(num):
    count_multi = 0
    for x in range(1, num+1):
        if num % x == 0:
            count_multi += 1
    if num == 1:
        print(f"O número {num} não é primo")
    elif count_multi > 2:
        print(f"O número {num} não é primo")
    else:
        print(f"O número {num} é primo")


valor = int(input("Digita um  número: "))
NumeroPrimo(valor)
