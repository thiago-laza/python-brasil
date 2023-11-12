'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver 
o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Informe o valor do salario: '))

print(50*'-')

if salario <= 280:
    aumento = salario*0.2
    salario_novo = salario + aumento
    print(f'Salario antes do reajuste: R$ {salario}')
    print('Percentual de aumenento: 20%')
    print(f'Valor do aumento: R$ {aumento}')
    print(f'Novo salario: R$ {salario_novo}')
elif salario > 280 and salario <= 700:
    aumento = salario*0.15
    salario_novo = salario + aumento
    print(f'Salario antes do reajuste: R$ {salario}')
    print('Percentual de aumento: 15%')
    print(f'Valor do aumento: R$ {aumento}')
    print(f'Novo salario: R$ {salario_novo}')
elif salario > 700 and salario < 1500:
    aumento = salario*0.1
    salario_novo = salario + aumento
    print(f'Salario antes do reajuste: R$ {salario}')
    print('Percentual de aumento: 10%')
    print(f'Valor do aumento: R$ {aumento}')
    print(f'Novo salario: R$ {salario_novo}')
elif salario >= 1500:
    aumento = salario*0.05
    salario_novo = salario + aumento
    print(f'Salario antes do reajuste: R$ {salario}')
    print('Percentual de aumento: 5%')
    print(f'Valor do aumento: R$ {aumento}')
    print(f'Novo salario: R$ {salario_novo}')

print(50*'-')