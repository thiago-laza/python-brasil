'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

num_1 = int(input('Digite o primeiro numero do intervalo: '))
num_2 = int(input('Digite o ultimo numero do intervalo: '))

if num_1 < num_2:
    for i in range(num_1+1,num_2):
        print(i)
elif num_2 < num_1:
    for i in range(num_1-1,num_2,-1):
        print(i)


