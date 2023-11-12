'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa 
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valor_hora = float(input('Informe o valor da hora trabalhada: '))
hora = float(input('Informe a quantidade de horas trabalhadas: '))

salario_bruto = valor_hora * hora

sindicato = salario_bruto*0.03
inss =  salario_bruto*0.1
fgts = salario_bruto*0.11

print(50*'-')

if salario_bruto <= 900:
    ir = 0
    descontos = sindicato + inss + ir
    salario_liquido = salario_bruto - descontos
    print(f'Salario bruto: R$ {salario_bruto}')
    print(f'IR (isento): R$ {ir}')
    print(f'Sindicato (3%): R$ {sindicato}')
    print(f'INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {descontos}')
    print(f'Salario liquido: R$ {salario_liquido}')
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = salario_bruto*0.05
    descontos = sindicato + inss + ir
    salario_liquido = salario_bruto - descontos
    print(f'Salario bruto: R$ {salario_bruto}')
    print(f'IR (5%): R$ {ir}')
    print(f'Sindicato (3%): R$ {sindicato}')
    print(f'INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {descontos}')
    print(f'Salario liquido: R$ {salario_liquido}')
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = salario_bruto*0.1
    descontos = sindicato + inss + ir
    salario_liquido = salario_bruto - descontos
    print(f'Salario bruto: R$ {salario_bruto}')
    print(f'IR (10%): R$ {ir}')
    print(f'Sindicato (3%): R$ {sindicato}')
    print(f'INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {descontos}')
    print(f'Salario liquido: R$ {salario_liquido}')
elif salario_bruto > 2500:
    ir = salario_bruto*0.2
    descontos = sindicato + inss + ir
    salario_liquido = salario_bruto - descontos
    print(f'Salario bruto: R$ {salario_bruto}')
    print(f'IR (20%): R$ {ir}')
    print(f'Sindicato (3%): R$ {sindicato}')
    print(f'INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {descontos}')
    print(f'Salario liquido: R$ {salario_liquido}')

print(50*'-')

    