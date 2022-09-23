lista = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def soma(x, n):
    # condição de parada
    if n == 0:
        return x[n]
    else:
        # recursão:
        return x[n] + soma(x, n-1)


print(f"Soma: {soma(lista, len(lista)-1)} ")
