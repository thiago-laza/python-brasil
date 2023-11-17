'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
 o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
 ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro 
 do álcool é R$ 1,90.
'''

quantidade = float(input('Informe a quantidade de combustivel: '))
tipo = input('Selecione o tipo de combustivel: A-Alcool ou G-Gasolina: ').upper()


if tipo == 'A':
    valor_pago = quantidade*1.9
    if quantidade <= 20:
        desconto = valor_pago*0.03
        valor_final = valor_pago - desconto
        print(f'Quantidade de alcool: {quantidade} litro\nValor: R$ {valor_pago}\nDesconto: R$ {desconto}\nValor final: R$ {valor_final}')
    else:
        desconto = valor_pago*0.05
        valor_final = valor_pago - desconto
        print(f'Quantidade de alcool: {quantidade} litro\nValor: R$ {valor_pago}\nDesconto: R$ {desconto}\nValor final: R$ {valor_final}')
elif tipo == 'G':
    valor_pago = quantidade*2.5
    if quantidade <= 20:
        desconto = valor_pago*0.04
        valor_final = valor_pago - desconto
        print(f'Quantidade de gasolina: {quantidade} litro\nValor: R$ {valor_pago}\nDesconto: R$ {desconto}\nValor final: R$ {valor_final}')
    else:
        desconto = valor_pago*0.06
        valor_final = valor_pago - desconto
        print(f'Quantidade de gasolina: {quantidade} litro\nValor: R$ {valor_pago}\nDesconto: R$ {desconto}\nValor final: R$ {valor_final}')

    
print('FIM.')