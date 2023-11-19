'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.'''

nome = input('Usuario: ')
senha = input('Senha: ')

while nome == senha:
    print('Erro!')
    nome = input('Usuario: ')
    senha = input('Senha: ')
    print('Usuario logado.')