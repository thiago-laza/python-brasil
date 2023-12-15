'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados 
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;'''
lista_notas = []
cont = 1


while True:
    notas = float(input(f'Nota {cont}: '))
    lista_notas.append(notas)
    cont+=1

    if notas == -1:
        lista_notas.pop()
        break
print('='*20)
print(f'Foram contabilizadas {len(lista_notas)} notas.')

print('='*20)
print('Os valores informados sao:')
for n in lista_notas:
    print(f'{n}',end=' ')

print()

print('='*20)
print('Os valores informados na ordem inversa sao:')
lista_notas_inversa = list(reversed(lista_notas))
for n in lista_notas_inversa:
    print(n)

print('='*20)
acu = 0
for n in lista_notas:
    acu+=n
print(f'A soma dos valores informados foi {acu}')

print('='*20)
media = acu/len(lista_notas)
print(f'A media dos valores digitados foi {media:.2f}')

print('='*20)
acu_acima_media = 0
for n in lista_notas:
    if n > media:
        acu_acima_media+=1
print(f'Foram identificadas {acu_acima_media} valores acima da media.')

print('='*20)
acu_abaixo = 0
for n in lista_notas:
    if n < 7:
        acu_abaixo+=1
print(f'Foram identificados {acu_abaixo} notas abaixo de 7.')
print('='*20)
print('Programa encerrado!')


