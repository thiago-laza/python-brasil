'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor 
médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

quantidade_cd = int(input('Informe a quantidade de CDs comprados: '))

cont = 1
acu = 0


while cont <= quantidade_cd:
    valor_cd = float(input(f'Informe o valor do {cont}⁰ CD: '))
    acu+=valor_cd
    cont+=1


media = acu/(cont-1)

print(f'O valor total investido foi de R$ {acu}. O valor medio de cada CD foi de R$ {media}')

