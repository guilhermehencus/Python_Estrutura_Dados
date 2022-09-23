# crie um programa que receba o nome do aluno e suas 5 médias, e depois imprima o nome do aluno, suas médias e a média final, que será calculada por uma função.

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
        media.append(float(input(f"Informe a média {y+1} do aluno: ")))
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
    print(f"Média final: {round(media_final[x], 3)}")
    x += 1
# crie um programa que calcule o imposto de renda sobre salários de uma pessoa, tomando por base o seu salário, o número de dependentes e sua contribuição para o INSS.


def inss(salario):
    if salario <= 1100.00:
        return salario*7.5/100
    elif salario <= 2203.48:
        inss = salario*9/100
        return inss
    elif salario <= 3305.22:
        return salario*12/100
    elif salario <= 6433.57:
        return salario*14/100
    else:
        return 6433.57*14/100


def faixa_imposto(salario):
    if salario <= 1903.98:
        return 0, 0
    elif salario >= 1903.99 and salario <= 2826.65:
        return 0.075, 142.80
    elif salario >= 2826.66 and salario <= 3751.05:
        return 0.15, 354.80
    elif salario >= 3751.06 and salario <= 4664.68:
        return 0.225, 636.13
    else:
        return 0.275, 869.36


salario = float(input("Informe o salário de contribuição: "))
n_dependentes = int(input("Informe o número de dependente: "))
inss(salario)
sal_base = salario - inss(salario) - (n_dependentes-189.59)
des_imposto_bruto = faixa_imposto(salario)[0]*salario
imposto_liquido = des_imposto_bruto - faixa_imposto(salario)[1]
print(f"O imposto líquido é: {round(imposto_liquido, 3)}")
# Faça um programa que obtenha a média final de um aluno nas 5 matérias que ele cursa


def CalculoMedia(nota):
    soma = 0
    for x in range(0, len(nota)):
        soma = soma+nota[x]
    media = soma/len(nota)
    return media


def situacao_aluno(notas):
    count_7 = 0
    count_5_7 = 0
    for x in notas:
        if x >= 7:
            count_7 = count_7+1
        elif x >= 5 and x < 7:
            count_5_7 += 1
        else:
            return "Reprovado direto"
    if count_7 == 5:
        return "Aprovado"
    elif count_5_7 >= 1 and count_5_7 <= 2:
        return "Conselho de classe"
    elif count_5_7 > 2:
        return "Reprovado"


media = []
y = 0
nome = input("informe o nome do aluno: ")
while y < 5:
    media.append(float(input(f"Informe a média do aluno na matéria{y+1}: ")))
    y += 1
situacao_aluno_final = situacao_aluno(media)
media_final = CalculoMedia(media)
print(f"O Aluno: {nome} está com sua situação: {situacao_aluno_final} e sua média final é: {round(media_final, 3)}")
# Faça um programa que receba uma lista de compras do cliente. O cliente deve digitar o código do item e a quantidade a comprar.


def total_compra(itens, quant, prec):
    soma = 0
    for x in itens:
        pos_list = int(itens.index(x))
        multi = int(prec[int(x)-1])*int(quant[pos_list])
        soma += multi
    return soma


lista_prec = [15, 10, 20, 25, 100, 50, 60, 5, 1]
lista_compra = []
lista_quant = []
x = 0
while x < 9:
    lista_compra.append(input("informe o código do item de 1 até 9: "))
    while int(lista_compra[x]) == 0 or int(lista_compra[x]) > 9:
        print("código inválido")
        val = str(lista_compra[x])
        lista_compra.remove(val)
        lista_compra.append(input("informe o código do item de 1 até 9: "))
    lista_quant.append(input("informe a quantidade do item: "))
    x += 1
Resultado = total_compra(lista_compra, lista_quant, lista_prec)
print(f"O valor total de todos os itens é: {Resultado}")
# Crie um programa para receber o número de lados de um polígono, e busque em uma lista o nome do polígono. A lista deve ter os seguintes itens


def poligono(nome_poli, num_poli):
    if num_poli <= 2 or num_poli > 8:
        print("O número informado de polígono não está disponivel ")
    else:
        soma_ang_int = (num_poli-2)*180
        med_ang_int = soma_ang_int/num_poli
        print(
            f"O  nome do polígono é: {nome_poli[numero_poligono-3]} tem {num_poli} lados, sua soma dos ângulos interno {soma_ang_int}° e o valor de cada ângulo {med_ang_int}°")


Lista_Poligono = ["TRIÂNGULO", "QUADRILÁTERO",
                  "PENTÁGONO", "HEXÁGONO", "HEPTÁGONO", "OCTÓGONO"]
numero_poligono = int(input(
    "Digite o lado de um polígono para descobrir o nome dele e também os ângulos"))
poligono(Lista_Poligono, numero_poligono)
# Questão 6: Descreva em linhas gerais o conceito de uma pilha, e quais são as 3 operações básicas que devem ser executadas em uma pilha (nome da operação e o que ela faz)
# Uma pilha é um tipo de lista que se baseia no funcionamento LIFO (Last In, First Out), ou seja, sua estrutura de inserção e remoção sempre se relaciona com o elemento mais recente da pilha.
# 3 operações: Top: consulta o elemento que se situa no topo da pilha, Push: inserir um novo elemento no topo da pilha, Pop: Remover o elemento localizado no topo da pilha.
