'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo 
que o usuário digite o salário inicial do funcionário.'''

salario_inicial = float(input('Salario inicial: '))
ano = int(input('Ano: '))
taxa = 0.015

for i in range(1995,ano):
    salario_atual = salario_inicial * (1 + taxa)
    salario_inicial = salario_atual
    taxa*=2

print(salario_atual)