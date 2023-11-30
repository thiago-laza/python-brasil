'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.'''

print('Informe a populacao de 2 paises e a taxa de crescimento anual da populacao para saber em quantos anos a populacao de um pais vai ultrapassar a outra.')

t = 0


populacao_a = float(input('Digite o numero de habitantes de pais A: '))
taxa_a = float(input('Digite a taxa de crescemento da populacao A em %: '))

populacao_b = float(input('Digite o numero de habitantes do pais B: '))
taxa_b = float(input('Digite a taxa de crescimento da populacao B em %: '))

while populacao_a > populacao_b:
    print('A populacao do pais A precisa ser menor que a populacao do pais B.')

    populacao_a = float(input('Digite o numero de habitantes de pais A: '))
    taxa_a = float(input('Digite a taxa de crescemento da populacao A em %: '))

    populacao_b = float(input('Digite o numero de habitantes do pais B: '))
    taxa_b = float(input('Digite a taxa de crescimento da populacao B em %: '))

    
while populacao_a <= populacao_b:
    populacao_a *= (1 + (taxa_a/100))
    populacao_b *= (1 + (taxa_b)/100)
    t+=1
    print(t,populacao_a,populacao_b)

print(f'A populacao do pais A vai ultrapassar a populacao do pais B em {t} anos.')