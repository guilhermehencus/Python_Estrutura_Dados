# Crie um programa que receba a medida dos lados de um triângulo, e que use uma função para descobrir que tipo de triângulo é.
def MedidaTriangulo(lado, lado2, lado3):
    if lado == lado2 and lado2 == lado3:
        print(f"O triângulo é Equilátelo")
    elif lado == lado2 and lado3 != lado and lado3 != lado2:
        print(f"O triângulo é Isósceles")
    elif lado == lado3 and lado2 != lado and lado3 != lado:
        print(f"O triângulo é Isósceles")
    elif lado2 == lado3 and lado2 != lado and lado3 != lado:
        print(f"O triângulo é Isósceles")
    else:
        print(f"O triângulo é Escaleno")


triangulo = int(input("Digite o primeiro lado: "))
triangulo2 = int(input("Digite o segundo lado: "))
triangulo3 = int(input("Digite o terceiro lado: "))
MedidaTriangulo(triangulo, triangulo2, triangulo3)
# Crie um programa que receba os dados de um cliente: Nome, RG, CPF e telefone e armazene em uma lista. Após receber todos os dados, você usar uma função para ler os dados e imprimir um a um.


def ImprimirDados(dados):
    x = 0
    print(f"O seu nome é {dados[x]} ")
    x += 1
    print(f"O seu RG é {dados[x]} ")
    x += 1
    print(f"O seu CPF é {dados[x]} ")
    x += 1
    print(f"O seu telefone é {dados[x]} ")


Lista_Dados = []
Nome = input("informe o nome do aluno: ")
Lista_Dados.append(Nome)
RG = int(input("informe o seu RG "))
Lista_Dados.append(RG)
CPF = input("informe o seu CPF: ")
Lista_Dados.append(CPF)
Telefone = input("informe o número de telefone: ")
Lista_Dados.append(Telefone)
ImprimirDados(Lista_Dados)
# Crie um programa que peça ao cliente para escolher o lanche de sua preferência 1 – Hamburguer com fritas, 2 – Hot dog completo, 3 – Cheeseburguer com fritas. Caso o usuário escolha um número diferente destes você deve informar que a opção é inválida, senão, deve informar o preço a pagar, conforme a escolha: 1 – 10,00, 2 – 20,00, 3 – 30,00.


def Pedidos(num_p):
    if num_p == 1:
        return 10.00
    if num_p == 2:
        return 20.00
    if num_p == 3:
        return 30.00


numero_pedido = int(input(
    "Digite o seu pedido 1 – Hamburguer com fritas ou 2 – Hot dog completo e 3 – Cheeseburguer com fritas. "))
if numero_pedido == 0 or numero_pedido > 3:
    print("Opção inválida ")
else:
    Resultado = Pedidos(numero_pedido)
    print(f"Você vai pagar: {Resultado} ")
# Crie um programa para receber o número de lados de um polígono, e busque em uma lista o nome do polígono. A lista deve ter os seguintes itens:
Lista_Poligono = ["TRIÂNGULO", "QUADRILÁTERO",
                  "PENTÁGONO", "HEXÁGONO", "HEPTÁGONO", "OCTÓGONO"]
numero_poligono = int(
    input("Digite o lado de um polígono para descobrir o nome dele"))
if numero_poligono <= 2 or numero_poligono > 8:
    print("O número informado de polígono não está disponivel ")
else:
    print(f"O nome do polígono é: {Lista_Poligono[numero_poligono-3]} ")
# Crie um programa que solicite ao cliente o valor a pagar, o número de parcelas e o meio de pagamento. Use uma função para calcular o valor de cada parcela, aplicando um desconto de 5% para o pagamento em dinheiro ou PIX.


def ValorDesconto(val):
    val = val*0.95
    return val


valor = float(input("informe valor que vai pagar : "))
parcelas = int(input("informe as parcelas"))
meio_pagamento = int(input(
    "informe o meio de pagamento digitando 1 – DÉBITO, 2 – CRÉDITO, 3 – PIX, 4 – DINHEIRO: "))
if parcelas > 12:
    while parcelas > 12:
        print("Quantidade inválida de parcelas ")
        parcelas = int(input("informe as parcelas corretamente"))
if meio_pagamento > 2:
    Resultado = ValorDesconto(valor)//parcelas
else:
    Resultado = valor//parcelas
print(f"O valor original é {valor} e o total a ser pago é: {Resultado} parcelado em {parcelas} vezes usando o número do pagamento {meio_pagamento}")
