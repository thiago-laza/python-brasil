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
    cedulas_100 = valor_saque // 100
    resto_1 = valor_saque - cedulas_100*100
    cedulas_50 = resto_1 // 50
    resto_2 = valor_saque - (cedulas_100*100 + cedulas_50*50)
    cedulas_10 = resto_2// 10
    resto_3 = valor_saque - (cedulas_100*100+cedulas_50*50 + cedulas_10*10)
    cedulas_5 = resto_3 // 5
    resto_4 = valor_saque - (cedulas_100*100+cedulas_50*50 + cedulas_10*10 + cedulas_5*5)
    cedulas_1 = resto_4
   

print(f'Para sacar R$ {valor_saque} sao necessarios {cedulas_100} cedulas de R$ 100,00, {cedulas_50} cedulas de R$ 50,00, {cedulas_10} cedulas de R$ 10,00, {cedulas_5} cedulas de R$ 5,00 e {cedulas_1} cedulas de R$ 1,00.')



  

                    





