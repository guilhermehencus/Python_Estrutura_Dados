'''
CALCULAR O FATORIAL DE UM NÚMERO

'''
n = int(input("Informe o número para cálculo do fatorial: "))
# FATORIAL DE UM NÚMERO É ELE MULTIPLICADO POR TODOS OS INTEIROS POSITIVOS QUE O ANTECEDEM
# FATORIAL DE 3:  3! = 3.2.1 = 6
# FATORIAL DE 4: 4! = 4.3.2.1 = 4 * 3! = 4 * 6 = 24
# FATORIAL DE 5: 5! = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 6 = 120
# FATORIAL DE 100: 100 * 99! -> 100 * 99 * 98! -> 100 * 99 * 98 * 97! ...
""" originalmente utilizariamos um laço de repetição para o cálculo:
 fatorial = 1
# LAÇO DE REPETIÇÃO
for x in range (1, n+1):
    fatorial = fatorial * x
print (f"Fatorial: {fatorial}") 
"""


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)


# fazendo um teste mesa:
# fatorial(5) -> return 5 * fatorial(4) -> return 5 * 24 -> 120
# fatorial(4) -> return 4 * fatorial(3) -> return 4 * 6 -> 24
# fatorial(3) -> return 3 * fatorial(2) -> return 3 * 2 -> 6
# fatorial(2) -> return 2 * fatorial(1) -> return 2 * 1 -> 2
# fatorial(1) -> return 1 * fatorial(0) -> return 1 * 1 -> 1
# fatorial(0) -> return 1
#
x = fatorial(n)

print(x)
""" USANDO RECURSIVIDADE, IMPLEMENTAR O CÁLCULO DE NÚMEROS DA SEQUÊNCIA
    DE FIBONACCI, QUE USA SEMPRE OS DOIS NÚMEROS ANTERIORES PARA CALCULAR O
    PRÓXIMO ELEMENTO DA SEQUÊNCIA:

# EXEMPLO: SEQUÊNCIA DE FIBONACCI...
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...  
"""
fibonacci = [0, 1, 1]


def sequenciaFibonacci(n):
    # condição de parada:
    if len(fibonacci) == n+1:
        fibonacci.remove(0)
        return fibonacci
    else:
        print(fibonacci[-1])
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
        return sequenciaFibonacci(n)


sequenciaFibonacci(n)
print(fibonacci)


""" IMPLEMENTAR A CONVERSÃO DE UM NÚMERO DECIMAL PARA BINÁRIO USANDO
    RECURSIVIDADE:

    PARA A CONVERSÃO DIVIDIMOS O NÚMERO POR 2 SUCESSIVAMENTE ATÉ O RESTO DA 
    DIVISÃO SER IGUAL A 1. OS RESTOS ANTERIORES SÃO CONSIDERADOS, EM ORDEM
    INVERSA, NA COMPOSIÇÃO DO NÚMERO BINÁRIO.
# CONVERSÃO DE UM NÚMERO DECIMAL PARA BINÁRIO...

#  EX: CONVERTER NÚMERO 8 PARA BINÁRIO:   8: 2 = 4 RESTO 0, 4: 2 = 2 RESTO 0, 2 : 2 = 1 E
    O RESTO É 0. 8 EM BINÁRIO = 1 0 0 0.
# SOMAR TODOS OS NÚMEROS ENTRE 1 E 100:
"""


def soma(n):  # EX.: soma(5) -> 5 + 4 + 3 + 2 + 1
    # condição de parada
    if n == 1:
        return n
    else:
        # recursão:
        return n + soma(n-1)


print(f"Soma: {soma(n)} ")

binario = []
print(type(binario))


def converteBinario(n):
    if n == 1:
        binario.insert(0, n)
    else:
        binario.insert(0, n % 2)

        return converteBinario(n//2)


converteBinario(n)
print(binario)
