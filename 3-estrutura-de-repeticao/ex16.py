'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a 
série até que o valor seja maior que 500.'''


x1 = 0
x2 = 1

print(f'{x1}\n{x2}')


cont = 0

while x1+x2 <= 500:
    x = x1 + x2
    x1 = x2
    x2 = x
    cont+= 1
    print(x)
