'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''


num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))

print(f'Qual operacao deseja realizar com {num_1} e {num_2}?')

print(' Adicao [1] \n Subtracao [2] \n Multiplicacao [3] \n Divisao [4]')

operacao = input('Operacao: ')

if operacao == '1':
    adicao = num_1 + num_2
    print(f'A adicao de {num_1} com {num_2} e igual a {adicao}')
    
    if adicao % 2 == 0:
        print(f'{adicao} e par.')
    else:
        print(f'{adicao} e impar.')
    
    if adicao > 0:
        print(f'{adicao} e positivo.')
    else:
        print(f'{adicao} e negativo.')

    if adicao // 1 == adicao:
        print(f'{adicao} e inteiro.')
    else:
        print(f'{adicao} e decimal.')
elif operacao == '2':
    subtracao = num_1 - num_2
    print(f'A subtracao de {num_1} com {num_2} e igual a {subtracao}')
    
    if subtracao % 2 == 0:
        print(f'{subtracao} e par.')
    else:
        print(f'{subtracao} e impar.')
    
    if subtracao > 0:
        print(f'{subtracao} e positivo.')
    else:
        print(f'{subtracao} e negativo.')

    if subtracao // 1 == subtracao:
        print(f'{subtracao} e inteiro.')
    else:
        print(f'{subtracao} e decimal.')
elif operacao == '3':
    multiplicacao = num_1 * num_2
    print(f'A multiplicacao de {num_1} com {num_2} e igual a {multiplicacao}')
    
    if multiplicacao % 2 == 0:
        print(f'{multiplicacao} e par.')
    else:
        print(f'{multiplicacao} e impar.')
    
    if multiplicacao > 0:
        print(f'{multiplicacao} e positivo.')
    else:
        print(f'{multiplicacao} e negativo.')

    if multiplicacao // 1 == multiplicacao:
        print(f'{multiplicacao} e inteiro.')
    else:
        print(f'{multiplicacao} e decimal.')
elif operacao == '4':
    divisao = num_1 / num_2
    print(f'A divisao de {num_1} com {num_2} e igual a {divisao}')
    
    if divisao % 2 == 0:
        print(f'{divisao} e par.')
    else:
        print(f'{divisao} e impar.')
    
    if divisao > 0:
        print(f'{divisao} e positivo.')
    else:
        print(f'{divisao} e negativo.')

    if divisao // 1 == divisao:
        print(f'{divisao} e inteiro.')
    else:
        print(f'{divisao} e decimal.')
else:
    print('Opcao invalida.')