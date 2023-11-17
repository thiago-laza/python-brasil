'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade 
(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

morango = float(input('Informe a quantidade de morango em kg: '))
maca = float(input('Informe a quantidade de maca em kg: '))



if morango <= 5:
    preco_morango = 2.5
    valor_pago_morango = morango*preco_morango
else:
    preco_morango = 2.2
    valor_pago_morango = morango*preco_morango

if maca <= 5:
    preco_maca = 1.8
    valor_pago_maca = maca*preco_maca
else:
    preco_maca = 1.5
    valor_pago_maca = maca*preco_maca

valor_total = valor_pago_morango + valor_pago_maca

print(f'Morango {morango} kg -> R$ {valor_pago_morango}\nMaca {maca} kg -> R$ {valor_pago_maca}\nTotal: R$ {valor_total}')

if morango + maca > 8 or valor_total > 25:
    desconto = valor_total*0.1
    valor_com_desconto = valor_total*0.9
    print(f'Desconto: R$ {desconto:.2f}\nValor com desconto: R$ {valor_com_desconto:.2f}')








