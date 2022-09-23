def soma_multi(num, count_num):
    if count_num == 1:
        return num
    else:
        return num + soma_multi(num, count_num-1)


num = int(input("Informe um número"))
num_2 = int(input("Informe outro número"))
if num > num_2:
    print(f"{num} x {num_2} é: {soma_multi(num_2, num)} ")
else:
    print(f"{num_2} x {num} é: {soma_multi(num, num_2)} ")
