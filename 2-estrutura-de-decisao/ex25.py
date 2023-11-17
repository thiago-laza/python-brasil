'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a 
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser 
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
 ele será classificado como "Inocente".'''


print('Responda SIM ou NAO par as perguntas abaixo:')

cont = 0

per1 = input('Telefonou para a vitima? ').upper()
if per1 == 'SIM':
    cont += 1
per2 = input('Esteve no local do crime? ').upper()
if per2 == 'SIM':
    cont += 1
per3 = input('Mora perto da vitima? ').upper()
if per3 == 'SIM':
    cont += 1
per4 = input('Devia para vitima? ').upper()
if per4 == 'SIM':
    cont += 1
per5 = input('Trabalhou com a vitima? ').upper()
if per5 == 'SIM':
    cont += 1

if cont <= 1:
    print('Nao e um suspeito.')
elif cont == 2:
    print('Suspeita')
elif cont >= 3 and cont <=4:
    print('Cumplice')
elif cont == 5:
    print('Assassino.')
