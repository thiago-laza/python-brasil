'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

num = int(input('Digite um numero inteiro menor que 1000: '))

centena_v = num // 100
dezena_v =  (num - centena_v*100) // 10
unidade_v = num - (centena_v*100 + dezena_v*10)


if centena_v == 1:
    nome_centena = 'centena'
else:
    nome_centena = 'centenas'

if dezena_v == 1:
    nome_dezena = 'dezena'
else:
    nome_dezena = 'dezenas'

if unidade_v == 1:
    nome_unidade = 'unidade'
else:
    nome_unidade = 'unidades'

if centena_v == 0 and dezena_v ==0:
    print(f'{unidade_v} {nome_unidade}')
elif centena_v == 0:
    print(f'{dezena_v} {nome_dezena} e {unidade_v} {nome_unidade}')
else:
    print(f'{centena_v} {nome_centena}, {dezena_v} {nome_dezena} e {unidade_v} {nome_unidade}')