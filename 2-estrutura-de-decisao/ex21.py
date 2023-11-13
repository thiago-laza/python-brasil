'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas 
notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 
reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 
e uma nota de 1;Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, 
quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

valor_saque = int(input('Informe o valor que deseja sacar: '))

if valor_saque < 10 or valor_saque > 600:
    print('Valor invalido. Permitido minimo de R$ 10,00 e maximo de R$ 600,00.')
else:
    if valor_saque > 100:
        notas_100 = valor_saque // 100
        rest_1 = valor_saque - notas_100*100
        if rest_1 >= 50:
            notas_50 = rest_1 // 50
            rest_2 = rest_1 - notas_50*50
        else:
            
            if rest_2 >= 10:
                notas_10 = rest_2 // 10
                rest_3 = rest_2 - notas_10*10
                if rest_3 >=5:
                    notas_5 = rest_3 // 5
                    rest_4 = rest_3 - notas_5*5
                    notas_1 = rest_4

print(notas_100,notas_50,notas_10,notas_5,notas_1)
                    





