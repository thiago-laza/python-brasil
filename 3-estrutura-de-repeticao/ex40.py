'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

acidente_maior = acidente_menor = cidade_maior = cidade_menor = None
acu = 0
acu_menor = 0
cont = 0

for c in range(5):
    cidade = int(input('Codigo da cidade: '))
    veiculos = int(input('Numero de veiculos: '))
    acu+=veiculos
    acidentes = int(input('Numero de acidentes: '))


    if acidente_maior is None or acidentes > acidente_maior:
        acidente_maior = acidentes
        cidade_maior = cidade

    if acidente_menor is None or acidentes < acidente_menor:
        acidente_menor = acidentes
        cidade_menor = cidade

    if veiculos < 2000:
        acu_menor+=acidentes
        cont+=1

media_veiculos = acu/5
media_menor = acu_menor/cont

print(f'O maior numero de acidentes foi de {acidente_maior} na cidade {cidade_maior}.')
print(f'O menor numero de acidentes foi de {acidente_menor} na cidade {cidade_menor}.')
print(f'A media de veiculos nas cinco cidades e de {media_veiculos}.')
print(f'A media de acidentes nas cidades com menos de 2000 veiculos e de {media_menor}.')