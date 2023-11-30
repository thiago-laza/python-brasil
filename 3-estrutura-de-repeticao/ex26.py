'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

eleitores = int(input('Informe o numero de eleitores: '))
print('Lista de candidatos:\nCandidato A\nCandidato B\nCandidato C')


cont_eleitores = 0
cont_candidato_a = 0
cont_candidato_b = 0
cont_candidato_c = 0
cont_nulos = 0

while cont_eleitores < eleitores:
    print(20*'-')
    voto = input(f'Eleitor {cont_eleitores+1}\nInforme seu voto: ').upper()
    print(20*'-')
    if voto == 'A':
        cont_candidato_a+=1
    elif voto == 'B':
        cont_candidato_b+=1
    elif voto == 'C':
        cont_candidato_c+=1
    else:
        cont_nulos+=1
    cont_eleitores+=1

print(20*'-')
print(f'Dos {eleitores} votos:\nCandidato A: {cont_candidato_a} votos\nCandidato B: {cont_candidato_b} votos\nCandidato C: {cont_candidato_c} votos\nVotos nulos: {cont_nulos} votos')
print(20*'-')
