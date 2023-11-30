'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar 
a série até o n−ésimo termo.'''

n = int(input('Digite um numero para gerar a sequencia de Fibonacci o numero digitado de termos: '))

while n < 0 or n > 46:
    n = int(input('Digite um numero maior que 0 e menor que 46 para gerar a sequencia de Fibonacci o numero digitado de termos: '))

x1 = 0
x2 = 1

print(f'{x1}\n{x2}')

for i in range(2,n):
    
    x = x1 + x2
    x1 = x2
    x2 = x

    print(x)

