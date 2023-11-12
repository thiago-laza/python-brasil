'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os 
valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os 
demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

print('Informe os valores dos coeficientes da equacao do segundo (ax²+bx+c=0)grau para obter suas raizes.')
a = float(input('Informe o valor do coeficiente a: '))
b = float(input('Informe o valor do coeficiente b: '))
c = float(input('Informe o valor do coeficiente c: '))

if a == 0:
    print('Coeficiente a = 0, logo nao e uma equacao do segudno grau.')
else:
    delta = (b**2) - 4*a*c
    if delta < 0:
        print(f'O valor do discriminante e negativo, logo a equacao {a}x²+{b}x+{c}=0 nao possui raizes reais.')
    else:
        x1 = (-1*b + delta**0.5)/2*a
        x2 = (-1*b - delta**0.5)/2*a
        if delta == 0:
            print(f'O discriminante e igual a zero, logo a equacao {a}x²+{b}x+{c}=0 possui duas raizes reais iguais. Raizes: {x1} e {x2}.')
        elif delta > 0:
            print(f'O discriminante e positivo, logo a equacao {a}x²+{b}x+{c}=0 possui duas raizes reais distintas. Raizes: {x1} e {x2}. ') 