'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a 
serem compradas e o preço total.'''

tamanho = float(input('Informe o tamanho em metros quadrados da area a ser pintada: '))

quantidade_tinta = tamanho/3

quantidade_latas = quantidade_tinta//18 + 1

valor_pago = quantidade_latas * 80

print(f'Para pintar uma regiao de {tamanho} m² sao necessarias {quantidade_latas} latas de tintas, custando R$ {valor_pago}.')

