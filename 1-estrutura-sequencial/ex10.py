'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

temperatura_c = float(input('Informe a temperatura em graus Celsius: '))

temperatura_f = ((temperatura_c/5)*9) + 32

print(f'A temperatura de {temperatura_c} ⁰C e equivalente a {temperatura_f} ⁰F.')