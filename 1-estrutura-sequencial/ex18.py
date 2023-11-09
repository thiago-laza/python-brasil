'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

arquivo = int(input('Informe o tamanho do arquivo em MB: '))
velocidade = int(input('Informe a velocidade da internet em Mbps: '))

conversao = arquivo * 8

tempo = (conversao // velocidade) // 60

print(f'O tempo de download de um aquivo de {arquivo} MB com uma conexao de {velocidade} Mbps e de aproximadamente {tempo} minutos.')