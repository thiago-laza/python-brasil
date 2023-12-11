'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 
13 anos possuem altura inferior à média de altura desses alunos.'''

vetor_idade = []
vetor_altura = []
for a in range(4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    vetor_idade.append(idade)
    altura = float(input('Altura: '))
    vetor_altura.append(altura)

acu = 0
for m in vetor_altura:
    acu+=m
media = acu/len(vetor_altura)

#obs: tentar por dicionario