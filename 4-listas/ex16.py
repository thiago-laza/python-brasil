'''Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
 ou seja, um total de $470.

Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos 
seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''

lista_funcionarios = []
cont = 1
while True:
    funcionario = {}

    funcionario['salario'] = 200
    funcionario['vendas'] = float(input(f'Valor das vendas do {cont}⁰ funcionario: '))
    funcionario['salario final'] = 200 + (1.09*funcionario['vendas'])
    cont+=1

    lista_funcionarios.append(funcionario)

    resp = input('Deseja cadastrar mais algum vendedor? [s/n]: ')
    if resp in 'Nn':
        break

cont_fun = 1
cont_int1 = cont_int2 = cont_int3 = cont_int4 = cont_int5 = cont_int6 = cont_int7 = cont_int8 = cont_int9 = 0
for funcionario in lista_funcionarios:
    print('-'*15)
    print(f'Funcionario {cont_fun}:')
    cont_fun+=1
    for j,k in funcionario.items():
        print(f'{j} {k}')
        if funcionario['salario final'] >= 200 and funcionario['salario final'] <300:
            cont_int1+=1
        elif funcionario['salario final'] >= 300 and funcionario['salario final'] <400:
            cont_int2+=1
        elif funcionario['salario final'] >= 400 and funcionario['salario final'] <500:
            cont_int3+=1
        elif funcionario['salario final'] >= 500 and funcionario['salario final'] <600:
            cont_int4+=1
        elif funcionario['salario final'] >= 600 and funcionario['salario final'] <700:
            cont_int5+=1
        elif funcionario['salario final'] >= 700 and funcionario['salario final'] <800:
            cont_int6+=1
        elif funcionario['salario final'] >= 800 and funcionario['salario final'] <900:
            cont_int7+=1
        elif funcionario['salario final'] >= 900 and funcionario['salario final'] <1000:
            cont_int8+=1
        elif funcionario['salario final'] >= 1000:
            cont_int9+=1

print('Faixa salarial:')

print(f'Foram identificados {cont_int1} salarios no intervalor $200 - $299')
print(f'Foram identificados {cont_int2} salarios no intervalor $300 - $399')
print(f'Foram identificados {cont_int3} salarios no intervalor $400 - $499')
print(f'Foram identificados {cont_int4} salarios no intervalor $500 - $599')
print(f'Foram identificados {cont_int5} salarios no intervalor $600 - $699')
print(f'Foram identificados {cont_int6} salarios no intervalor $700 - $799')
print(f'Foram identificados {cont_int7} salarios no intervalor $800 - $899')
print(f'Foram identificados {cont_int8} salarios no intervalor $900 - $999')
print(f'Foram identificados {cont_int9} salarios no intervalor $1000 ou mais.')








