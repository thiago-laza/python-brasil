'''Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de 
turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''

turmas = int(input('Informe o numero de turmas: '))

cont=0
acu = 0

while cont < turmas:
    alunos = int(input(f'Informe o numero de estudantes da {cont+1}⁰ turma: '))
    while alunos < 0 or alunos > 40:
        alunos = int(input(f'Valor invalido.Informe o numero de estudantes da {cont+1}⁰ turma: '))
    acu+=alunos
    cont+=1

media = acu/cont

print(f'A media de alunos das {cont} turmas e de {media} alunos por turma.')
