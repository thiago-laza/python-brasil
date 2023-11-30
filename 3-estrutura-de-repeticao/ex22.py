'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.'''


numero = int(input('Digite um numero inteiro para saber se ele e ou nao primo: '))

cont = 1
divisores = 0
divisores_np = []

while cont <= numero:
    
    if numero % cont == 0:
        divisores += 1
        divisores_np.append(cont)
    cont += 1
    
    

if divisores == 2:
    print(f'O numero {numero} e primo.')
    print(f'{numero} e divisivel por {divisores_np}')
else:
    print(f'O numero {numero} nao e um numero primo.')
    print(f'{numero} e divisivel por {divisores_np}')
   