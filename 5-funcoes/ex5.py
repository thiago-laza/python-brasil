'''Faça um programa com uma função chamada somaImposto. A função possui 
dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas 
expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.'''

def soma_imposto(taxa_imposto,custo):
    custo_final = custo*(1+taxa_imposto/100)
    print(f'Custo inicial do item: R$ {custo}')
    print(f'Taxa de imposto: {taxa_imposto}%')
    print(f'Custo final (depois de acrescentado o imposto): R$ {custo_final}')

valor_inicial = float(input('Informe o custo inicial do item: '))
taxa = float(input('Informe a taxa de imposto em %: '))
soma_imposto(taxa,valor_inicial)