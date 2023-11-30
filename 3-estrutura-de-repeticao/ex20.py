'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
limitando o fatorial a números inteiros positivos e menores que 16.'''

while True:

    numero = int(input('Digite um numero inteiro nao negativo para obter o seu fatorial: '))
    fatorial = numero

    while numero < 0 or numero >= 16:
        numero = int(input('Valor invalido. Digite um numero inteiro nao negativo e menor que 16 para obter o seu fatorial: '))


    produto = 1
    while numero > 0:
        produto *= numero
        numero -= 1
        if produto == numero - 1:
            break   

    print(f'O fatorial de {fatorial} e: {fatorial}! = {produto}')

    continuar = input('Deseja continuar calculando o fatorial [S/N]? ').upper()
    if continuar == 'S':
        True
    else:
        break