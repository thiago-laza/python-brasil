'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total 
do seu salário no referido mês.'''

valor_hora = float(input('Informe o valor recebido por cada hora trabalhada: '))
hora = float(input('Informe o numero de horas trabalhadas no mes: '))

salario = valor_hora * hora

print(f'O salario mensal de quem trabalha {hora} horas por mes e de R$ {salario}.')