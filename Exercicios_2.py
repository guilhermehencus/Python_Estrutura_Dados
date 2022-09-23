# Criar um programa que receba 5 notas de um aluno, armazenando-as em uma lista. Criar uma função que receba como parâmetro a lista de notas, e retorne a média aritmética.
import random


def CalculoMedia(nota):
    soma = 0
    for x in range(0, len(nota)):
        soma = soma+nota[x]
    media = soma/len(nota)
    return media


Notas = []
for y in range(0, 5):
    Notas.append(float(input(f"Digita a nota {y+1}: ")))
Resultado = CalculoMedia(Notas)
print(f"A média é: {round(Resultado, 3)}")
# Criar um programa que receba o nome de 10 pessoas e classifique em ordem crescente.
Nomes = ["João", "Marcelo", "Leonardo", "Franca", "Giovana",
         "Milena", "José", "Rafael", "Kayque", "David"]
print(sorted(Nomes))
# Dado um número real X e um número natural K, calcular a potência X elevado a K através de produtos sucessivos. x k = x.x.x.x. ...... x
x = float(input("Digita um número: "))
k = int(input("Digite o número expoente: "))
if x == 0 or x == 1:
    xk = x
else:
    xk = x**k
print(f"O resultado é: {xk}")
# Com relação a listas, Python dispõe de métodos específicos para a realização das diversas atividades referentes a lista. Descreva qual a forma de executar cada uma das atividades abaixo descritas, usando as estruturas de listas em Python e, quando houver, o método utilizado.
# Para fins de exemplo, considere uma lista com 10 elementos de nome lista e outra lista com 5 elementos de nome lista2 para exemplificar o uso.
Lista_1 = ["João", "Marcelo", "Leonardo", "Franca",
           "Giovana", "Milena", "José", "Rafael", "Kayque", "David"]
Lista_2 = ["Vinicius", "Marta", "Alex", "Greicy", "Arnaldo"]
# Acessar um elemento qualquer da lista;
print(random.choice(Lista_1))
print(random.choice(Lista_2))
# Inserir um elemento numa posição específica da lista;
Lista_1.insert(5, "Guilherme")
Lista_2.insert(2, "André")
# Remover um elemento de numa posição específica da lista;
Lista_1.pop(7)
Lista_2.pop(0)
# Combinar duas listas em uma única;
Lista_Total = Lista_1+Lista_2
print(Lista_Total)
# Particionar uma lista em duas;
Lista_Total.pop(2)
Lista_Total.pop(7)
Lista_Total.pop(1)
Lista_dividida = [Lista_Total[x:x + 6] for x in range(0, len(Lista_Total), 6)]
print(Lista_dividida)
Lista_1 = Lista_dividida[0]
Lista_2 = Lista_dividida[1]
# Obter cópia de uma lista;
Lista_1Nova = []
for itens in Lista_1:
    Lista_1Nova.append(itens)
print(Lista_1Nova)
# pode ser usado copy()
# Determinar o total de elementos na lista;
print(len(Lista_2))
# Ordenar elementos da lista;
print(sorted(Lista_1Nova))
# Procurar um determinado elemento na lista;;
print(Lista_1Nova[4])
print(Lista_2[1])
# Apagar uma lista.
del Lista_2
# Crie um programa que receba e armazene dados estatísticos da média de notas de uma escola e armazene em uma lista. A lista deve receber tantos elementos quanto necessário até que o usuário digite 0 como a média. Neste momento, obtenha a moda da lista usando uma função e a média da lista e exiba


def ModaMedia(nota):
    import statistics
    soma = 0
    Moda = statistics.mode(nota)
    for x in range(0, len(nota)):
        soma = soma+nota[x]
    media = soma/len(nota)
    print(f" A média é {round(media, 3)} e a moda é {Moda}")


Notas = []
count = 1
count_nota = 1
while (count != 0):
    Notas.append(
        float(input(f"Digita a nota {count_nota} ou digite zero para parar: ")))
    count = Notas[count_nota-1]
    count_nota += 1
if 0 in Notas:
    Notas.remove(count)
    ModaMedia(Notas)
# Crie um programa que receba dois números e ache todos os números primos existentes no intervalo entre os dois números informados.


def NumeroPrimo(num, num2):
    for x in range(num, num2+1):
        count_multi = 0
        for y in range(1, x+1):
            if x % y == 0:
                count_multi += 1
        if count_multi <= 2:
            print(f"O número {x} é primo")
            count_multi = 0


numero = int(input("Digita um número: "))
numero2 = int(input("Digite um outro número: "))
NumeroPrimo(numero, numero2)
# CRIE UM PROGRAMA QUE RECEBA O NOME DO ALUNO E SUAS 5 MÉDIAS, E DEPOIS IMPRIMA O NOME DO ALUNO,
# SUAS MÉDIAS E A MÉDIA FINAL, QUE SERÁ CALCULADA POR UMA FUNÇÃO.


def CalculoMedia(nota):
    soma = 0
    for x in range(0, len(nota)):
        soma = soma+nota[x]
    media = soma/len(nota)
    return media


nome = []
media = []
media_final = []
x = 0
while x < 5:
    nome.append(input("informe o nome do aluno: "))
    y = 0
    while y < 5:
        media.append(int(input("Informe a média do aluno: ")))
        y += 1
    x += 1

x = 0
Media_Divida_Aluno = [media[x:x + 5] for x in range(0, len(media), 5)]
while x < 5:
    media_final.append(CalculoMedia(Media_Divida_Aluno[x]))
    x += 1
x = 0
while x < 5:
    print(f"Aluno: {nome[x]}")
    print(f"Médias dos 5: {Media_Divida_Aluno[x]}")
    print(f"Média final: {media_final[x]}")
    x += 1
