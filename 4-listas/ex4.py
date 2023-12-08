'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes.'''

'''
letras = ['a','b','c','d','e','f','g','h','i','j']
consoantes = 'bcdfghj'

print(f'No vetor {letras} as consoantes sao: ')
print()
cont = 0
for l in letras:
    if l in consoantes:
        cont+=1
        print(l)

print()
print(f'Foram identificadas {cont} consoantes.')
'''
        
vetor_geral = []
for i in range(10):
    letras_usuarios = input('Digite uma letra: ')
    vetor_geral.append(letras_usuarios)

quantidade_consoantes = 0
consoantes = []

for letras_usuarios in vetor_geral:
    verificador = 'bcdfghjklmnpqrstvxzwy'
    if letras_usuarios in verificador:
        quantidade_consoantes += 1
        consoantes.append(letras_usuarios)

print(consoantes)
print(quantidade_consoantes)






    