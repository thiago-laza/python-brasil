'''Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.'''

# Solicita ao usuário o número do andar
andar_desejado = int(input("Digite o número do andar desejado: "))

# Inicia a contagem do primeiro andar válido
andar_atual = 1

# Inicia o contador de andares válidos
chao = andar_desejado

while chao > 0:
    # Converte o número do andar atual para string e verifica se contém '4' ou '13'
    if '4' not in str(andar_atual) and '13' not in str(andar_atual):
        chao -= 1  # Reduz o contador de andares válidos
    andar_atual += 1  # Passa para o próximo andar

# Exibe o resultado
print(f"O número atribuído ao andar {andar_desejado} é {andar_atual - 1}.")