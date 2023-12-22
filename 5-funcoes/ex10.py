'''Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, 
obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira 
jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando 
os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este 
Ponto novamente.'''
import random


def dado(a, b):
    return num_1 + num_2


def natural():
    if dado(num_1, num_2) == 7 or dado(num_1, num_2) == 11:
        print(f'{dado(num_1, num_2)} Natural - GANHOU!')


def craps():
    if dado(num_1, num_2) == 2 or dado(num_1, num_2) == 3 or dado(num_1, num_2) == 12:
        print(f'{dado(num_1, num_2)} Craps - PERDEU!')


def ponto():
    print(f'{dado(num_1, num_2)} jogando')


num_1 = random.randint(1, 6)
num_2 = random.randint(1, 6)


natural()
craps()
ponto()





