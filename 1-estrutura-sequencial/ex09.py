'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).'''

temperatura_f = float(input('Informe a temperatura em Fahrenheit: '))

temperatura_c = 5 * ((temperatura_f - 32)/9)

print(f'A temperatura de {temperatura_f} ⁰F e equivalente a {temperatura_c} ⁰C')