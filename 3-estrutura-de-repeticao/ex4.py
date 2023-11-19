'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.'''

t = 0

populacao_a = 80000
taxa_a = 1.03

populacao_b = 200000
taxa_b = 1.015

while populacao_a <= populacao_b:
    populacao_a *= taxa_a
    populacao_b *= taxa_b
    t+=1
    print(t,populacao_a,populacao_b)

print(f'A populacao do pais A vai ultrapassar a populacao do pais B em {t} anos.')
    




