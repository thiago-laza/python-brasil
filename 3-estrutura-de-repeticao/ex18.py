'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

quantidade = int(input('Informe a quantidade de numeros que serao digitados: '))

while quantidade <=0:
   quantidade = int(input('Valor nao permitido. Informe a quantidade de numeros que serao digitados: ')) 

primeiro_numero = float(input('Digite o 1⁰ numero: '))

menor_numero = primeiro_numero
maior_numero = primeiro_numero
acumulador = primeiro_numero

for i in range(2,quantidade+1):
   numero = float(input(f'Digite o {i}⁰ numero: '))

   acumulador += numero

   if numero > maior_numero:
      maior_numero = numero
   elif numero < menor_numero:
      menor_numero = numero

print(menor_numero,maior_numero,acumulador)
   
   