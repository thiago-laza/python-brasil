'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''


valor_hora = float(input('Informe o valor recebido por hora trabalhada: '))
hora = float(input('Informe o numero de horas trabalhadas no mes: '))

salario_bruto = valor_hora * hora
desconto_ir = salario_bruto*0.11
desconto_inss = salario_bruto*0.08
desconto_sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - (desconto_ir+desconto_inss+desconto_sindicato)

print(f'Salario bruto: R$ {salario_bruto}.')
print(f'Desconto de IR: R$ {desconto_ir}')
print(f'Desconto de INSS: R$ {desconto_inss}.')
print(f'Desconto de sindicato: R$ {desconto_sindicato}.')
print(f'Salario liquido: R$ {salario_liquido}')



