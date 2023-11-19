'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = input('Nome: ')
while len(nome) <= 3:
    nome = input('Nome invalido, digite novamento o nome com mais de 3 caracteres:')

idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade invalida, informe uma idade entre 0 e 150: '))

salario = float(input('Salario: '))
while salario < 0:
    salario = float(input('Salario invalido, informe um salario maior que zero: '))

sexo = input('Sexo: ')
while sexo != 'f' and sexo != 'm':
    sexo = input('Sexo invalido, infome masculino (m) ou feminino (f): ')

estado_civil = input('Informe o estado civil: ')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Estado civil invalido, informe solteiro (s), casado (c), viuvo (v) ou divorsiado (d): ')


print(30*'-')
print(f'Nome: {nome}\nIdade: {idade}\nSalario: R$ {salario}\nSexo: {sexo}\nEstado civil: {estado_civil}')
print(30*'-')