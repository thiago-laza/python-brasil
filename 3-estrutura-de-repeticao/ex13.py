'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao 
segundo número. Não utilize a função de potência da linguagem.'''


base = float(input('Base: '))
expoente = int(input('Expoente: '))

potencia = 1#comeca com esse valor, pois precisa ter um valor inicial para receber o incremento no for.

for i in range(expoente):#o i vai ate o expoente, ou seja ele vai multiplicar a base por ela mesma i vezes
    potencia *= base# o incremento: quando i for 1 -> base, quando i for 2 -> base*base... a ultima vez sera o resultado que se espera.

print(potencia)

'''
exemplo:

base = float(input('Base: ')) -> 2
expoente = int(input('Expoente: '))-> 3

potencia = 1

for i in range(expoente): |i=0|i=1|i=2|
    potencia *= base (potencia = potencia * base)|potencia=1*2|potencia = 2*2|potencia=4*2|

print(potencia)-> 8
'''



    

    

