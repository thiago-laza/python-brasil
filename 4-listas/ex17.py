'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será 
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco 
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme 
o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

lista_atletas = []#cria a lista geral

while True:
    nome = input('Nome: ')

    if not nome.strip():
        break

    saltos = []#vai armazenar o valor dos saltos

    acu_saltos = 0
    sequencia = ['primeiro','segundo','terceiro','quarto','quinto']
    for s in range(5):
        salto = float(input(f'{sequencia[s]} salto: '))
        acu_saltos+=salto
        saltos.append(salto)#inserindo os valores dos saltos

    media_saltos = acu_saltos/len(saltos)

    atleta ={#dicionario
        'nome':nome,
        'saltos':saltos,
        'media':media_saltos
    }
    lista_atletas.append(atleta)#inserindo na lista geral os dicionarios

print('Resultado final:')
print('-'*25)
for atleta in lista_atletas:
    print(f"Nome: {atleta['nome']}")
    print(f"Saltos: {atleta['saltos']}")
    print(f"Media dos saltos: {atleta['media']}")
    print('-'*25)









