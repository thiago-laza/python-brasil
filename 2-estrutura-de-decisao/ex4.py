'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = str(input('Digite uma letra: '))

vogais = ["a","e","i","o","u"]


if letra.isalpha():
    if letra in vogais:
        print(f'A letra {letra} e uma vogal.')
    else:
        print(f'A letra {letra} e uma consoante.')
else:
    print(f'{letra} nao e uma letra.')