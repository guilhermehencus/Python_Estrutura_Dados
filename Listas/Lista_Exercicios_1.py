# Faça um programa que leia dois valores e informe a média entre eles. (use float como tipo de dado).
valor1 = float(input("Digita o primeiro valor:"))
valor2 = float(input("Digita o segundo valor:"))
media = (valor1+valor2)/2
print(f"A média é: {media}")
# Faça um programa que leia uma temperatura em graus Centígrados e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, onde F é a temperatura em Fahrenheit e C em graus Centígrados
val_celsius = float(input("Digita o valor em celsius:"))
val_fahrenheit = (9 * val_celsius + 160) / 5
print(f"O valor convertido é: {val_fahrenheit}")
# Faça um programa que leia uma temperatura em graus Centígrados e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, onde F é a temperatura em Fahrenheit e C em graus Centígrados
# Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula: VOLUME = 3.14159 * R2 * ALTURA.
val_raio = int(input("Digita o valor do raio:"))
val_altura = float(input("Digita o valor da altura:"))
volume = 3.14159 * (val_raio*val_raio) * val_altura
print(f"O valor do volume é: {volume}")
# Faça um programa que leia 5 valores e informe o valor do maior.
val_1 = int(input("Digita o valor 1:"))
val_2 = int(input("Digita o valor 2:"))
val_3 = int(input("Digita o valor 3:"))
val_4 = int(input("Digita o valor 4:"))
val_5 = int(input("Digita o valor 5:"))
if val_1 > val_2 and val_1 > val_3 and val_1 > val_4 and val_1 > val_5:
    print(f"O maior valor é: {val_1}")
elif val_2 > val_1 and val_2 > val_3 and val_2 > val_4 and val_2 > val_5:
    print(f"O maior valor é: {val_2}")
elif val_3 > val_1 and val_3 > val_2 and val_3 > val_4 and val_3 > val_5:
    print(f"O maior valor é: {val_3}")
elif val_4 > val_1 and val_4 > val_2 and val_4 > val_3 and val_4 > val_5:
    print(f"O maior valor é: {val_4}")
else:
    print(f"O maior valor é: {val_5}")
#  Solicitar o consumo médio de um veículo, bem como o tempo de viagem e a velocidade média. Com base nestas informações: Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem
val_k_litro_auto = int(input("Coloca o valor rodado do carro em km/l:"))
val_tempo = int(input("Coloca o tempo na viagem: "))
val_velo_media = int(input("Coloca a velocidade média:"))
val_distancia = val_tempo*val_velo_media
val_litros_usado = val_distancia/val_k_litro_auto
print(f"Velocidade média: {val_velo_media}")
print(f"Tempo gasto da viagem: {val_tempo}")
print(f"Distancia percorrida: {val_distancia}")
print(f"Litros utilizados durante a viagem: {val_litros_usado}")
