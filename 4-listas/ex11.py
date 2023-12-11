'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.'''
primeiro_vetor = []
segundo_vetor = []
terceiro_vetor = []
vetor = []
print('Primeiro vetor:')
for i in range(10):
    valor_primeiro = int(input(f'Digite o valor {i}: '))
    primeiro_vetor.append(valor_primeiro)
print(primeiro_vetor)

print('Segundo vetor:')
for j in range(10):
    valor_segundo = int(input(f'Digite o valor {j}: '))
    segundo_vetor.append(valor_segundo)
print(segundo_vetor)

print('Terceiro vetor:')
for t in range(10):
    valor_terceiro = int(input(f'Digite o valor {t}: '))
    terceiro_vetor.append(valor_terceiro)
print(terceiro_vetor)

print('Intercalando elementos dos dois vetores teremos:')

for p,s,t in zip(primeiro_vetor,segundo_vetor,terceiro_vetor):
    vetor.append(p)
    vetor.append(s)
    vetor.append(t)
print(vetor)