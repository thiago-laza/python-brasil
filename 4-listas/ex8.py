'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.'''
vetor_idade = []
vetor_altura = []
for p in range(5):
    idade = int(input('Digite a idade: '))
    vetor_idade.append(idade)
    altura = float(input('Digite a altura: '))
    vetor_altura.append(altura)
print('As idades na ordem inversa sao:')
for idade in reversed(vetor_idade):
    print(idade)
print('As alturas na ordem inversa sao:')
for altura in reversed(vetor_altura):
    print(altura)