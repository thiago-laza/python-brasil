'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos 
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

primeiro_vetor = []
segundo_vetor = []
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

print('Intercalando elementos dos dois vetores teremos:')

for p,s in zip(primeiro_vetor,segundo_vetor):
    vetor.append(p)
    vetor.append(s)
print(vetor)
    
