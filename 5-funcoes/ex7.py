'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por 
uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação 
e o número de dias em atraso e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa 
deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado 
um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, 
exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações 
pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos 
sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, 
mais 0,1% de juros por dia de atraso.'''
def valor_pagamento(p,d):
    prestacao_total=0
    if d > 0:
        return p*(1.03) + p*(0.001)*d
    else:
        return p


total = 0
cont = 0

while True:
    prestacao = float(input('Prestacao: R$ '))
    dias = int(input('Dias de atraso: '))
    cont+=1
    print(f'{valor_pagamento(prestacao,dias)}')
    total+=valor_pagamento(prestacao,dias)
    resp = input('Deseja inserir mais alguma informacao?[s/n] ')
    if resp in 'n':
        print(f'Foram cadastradas {cont} prestacoes.')
        print(f'O valor total das prestacoes foi de {total}')
        break







