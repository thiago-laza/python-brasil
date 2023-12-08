'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

notas = [3,4,5,6]

acu = 0

for i in notas:
    acu+=i

media = acu/len(notas)

print(f'A media das notas {notas} e igual a {media}')