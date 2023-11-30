'''Altere o programa anterior para mostrar no final a soma dos números.'''

num_1 = int(input('Digite o primeiro numero do intervalo: '))
num_2 = int(input('Digite o ultimo numero do intervalo: '))

acumulador = 0

if num_1 < num_2:
    for i in range(num_1+1,num_2):
        acumulador += i
        print(i)
elif num_2 < num_1:
    for i in range(num_1-1,num_2,-1):
        acumulador += i
        print(i)

print(f'A soma dos valores da sequencia e igual a {acumulador}.')