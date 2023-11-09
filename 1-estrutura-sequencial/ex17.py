'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias.'''

tamanho = float(input('Informe a medida da area a ser pintada em metros quadrados: '))

quantidade_tinta = tamanho/6

quantidade_lata_1 = quantidade_tinta//18 + 1
quantidade_lata_2 = quantidade_tinta//3.6 + 1

valor_lata_1 = quantidade_lata_1 * 80
valor_lata_2 = quantidade_lata_2 * 25

print('SITUACAO 1: LATAS DE 18 LITROS')
print(f'Para pintar uma regiao com {tamanho} m² sao necessarias {quantidade_lata_1} latas ao custo de R$ {valor_lata_1}')

print('SITUACAO 2: LATAS DE 3.6 LITROS')
print(f'Para pintar uma regiao com {tamanho} m² sao necessarias {quantidade_lata_2} latas ao custo de R$ {valor_lata_2}')

print('SITUACAO 3: MISTURAR LATAS DE 18 LITROS E 3.6 LITROS.')

quantidade_tinta_2 = (tamanho/6)*1.1
quantidade_lata_otimizada = quantidade_tinta_2//18 + ((((quantidade_tinta_2/18) - (quantidade_tinta_2//18)) // 3.6) + 1)
quantidade_lata_1_2 = quantidade_tinta_2//18
quantidade_lata_2_2 = ((((quantidade_tinta_2/18) - (quantidade_tinta_2//18)) // 3.6) + 1)
valor_otmizado = (quantidade_tinta_2//18)*80 + (((((quantidade_tinta_2/18) - (quantidade_tinta_2//18)) // 3.6) + 1))*25

print(f'Para pintar uma regiao com {tamanho} m² serao necessarias {quantidade_lata_1_2} latas de 18 litros e {quantidade_lata_2_2} latas de 3.6 litros, custando R$ {valor_otmizado}. ')