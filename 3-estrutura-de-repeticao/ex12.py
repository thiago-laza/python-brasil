'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual 
numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50'''

num = int(input('Informe um numero para obter sua tabuada: '))

while num <= 0 or num > 10:
    num = int(input('Informe um numero maior que zero e menor que 10 para obter sua tabuada: '))

print(20*'-')
for i in range(1,11):
    produto = i * num
    print(f'{i} X {num} = {produto}')
print(20*'-')
