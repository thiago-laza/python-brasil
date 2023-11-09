'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes 
fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

altura = float(input('Informe sua altura: '))

peso_ideal_h = (72.7*altura) - 58
peso_ideal_m = (62.1*altura) - 44.7

print(f'Uma pessoa que tem {altura} m de altura tem peso ideal de {peso_ideal_h} kg se for homem e de {peso_ideal_m} kg se for mulher.')

