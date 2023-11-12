'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo 
que a decisão é sempre pelo mais barato.'''

prod_1 = float(input('Digite o valor do primeiro produto: '))
prod_2 = float(input('Digite o valor do segundo produto: '))
prod_3 = float(input('Digite o valor do terceiro produto: '))

if prod_1 > prod_2 and prod_2 > prod_3:
    print(f'Dos produtos pesquisados: R$ {prod_1}, R$ {prod_2} e R$ {prod_3}, o mais caro e R$ {prod_1} e o mais barato e R$ {prod_3}. Comprar o terceiro R$ {prod_3}')
elif prod_1 > prod_3 and prod_3 > prod_2:
    print(f'Dos produtos pesquisados: R$ {prod_1}, R$ {prod_2} e R$ {prod_3}, o mais caro e R$ {prod_1} e o mais barato e R$ {prod_2}. Comprar o segundo R$ {prod_2}')
elif prod_2 > prod_1 and prod_1 > prod_3:
    print(f'Dos produtos pesquisados: R$ {prod_1}, R$ {prod_2} e R$ {prod_3}, o mais caro e R$ {prod_2} e o mais barato e R$ {prod_3}. Comprar o terceiro R$ {prod_3}')
elif prod_2 > prod_3 and prod_3 > prod_1:
    print(f'Dos produtos pesquisados: R$ {prod_1}, R$ {prod_2} e R$ {prod_3}, o mais caro e R$ {prod_2} e o mais barato e R$ {prod_1}. Comprar o primeiro R$ {prod_1}')
elif prod_3 > prod_1 and prod_1 > prod_2:
    print(f'Dos produtos pesquisados: R$ {prod_1}, R$ {prod_2} e R$ {prod_3}, o mais caro e R$ {prod_3} e o mais barato e R$ {prod_2}. Comprar o segundo R$ {prod_2}')
elif prod_3 > prod_2 and prod_2 > prod_1:
    print(f'Dos produtos pesquisados: R$ {prod_1}, R$ {prod_2} e R$ {prod_3}, o mais caro e R$ {prod_3} e o mais barato e R$ {prod_1}. Comprar o primeiro R$ {prod_1}')