'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada 
por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))

media = (nota_1 + nota_2 + nota_3)/3

if media < 7:
    print(f'Reprovado, sua media foi: {media}')
elif media >= 7 and media < 10:
    print(f'Aprovado, sua media foi : {media}')
elif media == 10:
    print(f'Aprovado com distincao, sua media foi {media}')
else:
    print('Informacoes invalidas.')