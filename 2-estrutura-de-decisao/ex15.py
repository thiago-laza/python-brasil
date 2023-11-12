'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

medida_1 = float(input('Informe a primeira medida: '))
medida_2 = float(input('Informe a segunda medida: '))
medida_3 = float(input('Informe a terceira medida: '))

if (medida_1 < medida_2 + medida_3) and (medida_2 < medida_1 + medida_3) and (medida_3 < medida_1 + medida_2):
    print(f'As medidas {medida_1}, {medida_2} e {medida_3} formam um triangulo.')
    if medida_1 == medida_2 and medida_2 == medida_3:
        print(f'Esse triangulo e classificado como equilatero.')
    elif medida_1 == medida_2 and medida_2 != medida_3:
        print(f'Esse triangulo e classificado como isosceles.')
    else:
        print(f'Esse triangulo e classificado como escaleno.')
else:
    print(f'As medidas {medida_1}, {medida_2} e {medida_3} nao formam um triangulo.')