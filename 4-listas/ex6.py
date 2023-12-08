'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.'''

lista_media =[]
for a in range(4):
    nome = input('Nome: ')
    acu=0
    cont=0
    for n in range(4):
        nota = float(input('Nota: '))
        cont+=1
        acu+=nota
    media = acu/cont
    lista_media.append(media)
cont_media=0
for m in lista_media:
    if m >= 7:
        cont_media+=1
print(f'A lista de medias sao: {lista_media}')
print(f'Foram contabilizadas {cont_media} medias maior ou igual a 7.')



