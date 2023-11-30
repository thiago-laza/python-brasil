'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de 
idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, 
conforme a média calculada.'''

numero_pessoas = int(input('Informe o numero de pessoas: '))

cont = 0
acu = 0 

while cont < numero_pessoas:
    idade = int(input(f'Informe a idade da {cont+1}⁰ pessoa: '))
    acu+=idade
    cont+=1

media = acu/cont

if media <= 25:
    print(f'As {cont} pessoas possuem uma media de idade de {media:.1f} anos e sao classificadas como jovens.')
elif media > 25 and media <=60:
    print(f'As {cont} pessoas possuem uma media de idade de {media:.1f} anos e sao classificadas com adultas.')
else:
    print(f'As {cont} pessoas possuem uma media de idade de {media:.1f} anos e sao classificadas como idosas.')
