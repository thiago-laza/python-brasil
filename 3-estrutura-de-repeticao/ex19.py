'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

quantidade = int(input('Informe a quantidade de numeros que serao digitados: '))

while quantidade <=0:
   quantidade = int(input('Valor nao permitido. Informe a quantidade de numeros que serao digitados: ')) 

primeiro_numero = float(input('Digite o 1⁰ numero: '))

if primeiro_numero < 0 or primeiro_numero > 1000:
   while primeiro_numero < 0 or primeiro_numero > 1000:
      primeiro_numero = float(input('Valor invalido, digite o 1⁰ numero: '))

menor_numero = primeiro_numero
maior_numero = primeiro_numero
acumulador = primeiro_numero

for i in range(2,quantidade+1):
   numero = float(input(f'Digite o {i}⁰ numero: '))
   while numero < 0 or numero > 1000:
      numero = float(input(f'Valor invalido, digite o {i}⁰ numero: '))

   acumulador += numero

   if numero > maior_numero:
      maior_numero = numero
   elif numero < menor_numero:
      menor_numero = numero

print(menor_numero,maior_numero,acumulador)