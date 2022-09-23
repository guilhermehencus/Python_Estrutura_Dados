# CRIAR UM PROGRAMA PARA RECEBER 3 NOTAS E CALCULAR A MÉDIA DELAS POR MEIO DE UMA FUNÇÃO
def CalculoMedia(nota1, nota2, nota3):
    media = (nota1+nota2+nota3)/3
    print(f"A média é: {media}")


valor1 = float(input("Digita o primeiro valor:"))
valor2 = float(input("Digita o segundo valor:"))
valor3 = float(input("Digita o terceiro valor:"))
CalculoMedia(valor1, valor2, valor3)
# CRIAR UM PROGRAMA PARA RECEBER O VALOR DA TEMPERATURA EM CÉLSIUS E CALCULAR EM FAHRENHEIT USANDO UMA FUNÇÃO


def CelsiusFahrenheit(val_celsius):
    val_fahrenheit = (9 * val_celsius + 160) / 5
    print(f"O valor convertido é: {val_fahrenheit}")


val_receb_celsius = float(input("Digita o valor em celsius:"))
CelsiusFahrenheit(val_receb_celsius)
# CRIAR UM PROGRAMA QUE SOME TODOS OS NÚMEROS ENTRE 1 E 2000.
soma = 0
for x in range(1, 2001, 1):
    soma += x
print(f"A soma de 1 e 2000 é: {soma}")
x = 0
soma = 0
while x < 2001:
    soma += x
    x += 1
print(f"A soma de 1 e 2000 é: {soma}")
# CRIAR UM PROGRAMA QUE SOME TODOS OS NÚMEROS MÚLTIPLOS DE 3 ENTRE 1 E 100.
soma = 0
for x in range(1, 101):
    if x % 3 == 0:
        soma += x
print(f"A soma de todos os números múltiplos de 3: {soma}")
# receber frase e contar a quantidade de 'a'
frase = input("Digite uma frase")
y = 0
for x in frase:
    if x == "a":
        y += 1
print(f"A quantidade de 'a' na frase {frase}: {y}")
