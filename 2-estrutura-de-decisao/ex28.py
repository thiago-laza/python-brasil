'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a 
quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e 
quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

tipo = input('Informe o tipo de carne desejada:\n[1] File Duplo\n[2]Alcatra\n[3]Picanha\nTipo: ')
quantidade = float(input('Informe a quantidade em kg desejada: '))

if tipo == '1':
    tipo_carne = 'File Duplo'
    if quantidade <= 5:
        valor_pago = quantidade*4.9
    else:
        valor_pago = quantidade*5.8
elif tipo == '2':
    tipo_carne = 'Alcatra'
    if quantidade <= 5:
        valor_pago = quantidade*5.9
    else:
        valor_pago = quantidade*6.8
elif tipo == '3':
    tipo_carne = 'Picanha'
    if quantidade <= 5:
        valor_pago = quantidade*6.9
    else:
        valor_pago = quantidade*7.8
else:
    print('Informacao invalida.')

forma_de_pagamento = input('Informe a forma de pagamento: \n[1]Dinheiro\n[2]Cartao Tabajara\nPagamento: ')

if forma_de_pagamento == '1':
    tipo_de_pagamento = 'Dinheiro'
    desconto = 0
    valor_final = valor_pago - desconto
elif forma_de_pagamento == '2':
    tipo_de_pagamento = 'Cartao'
    desconto = valor_pago*0.05
    valor_final = valor_pago - desconto
else:
    print('Informacao invalida.')


print(20*'-')
print('CUPOM FISCAL')
print(f'Tipo de carne: {tipo_carne}\nQuantidade de carne: {quantidade} Kg\nPreco total: R$ {valor_pago:.2f}\nTipo de pagamento: {tipo_de_pagamento}\nDesconto: R$ {desconto:.2f}\nValor Final: R$ {valor_final:.2f}')
print(20*'-')