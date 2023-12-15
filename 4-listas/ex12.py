'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 
13 anos possuem altura inferior à média de altura desses alunos.'''



lista_pessoas = []
acu_altura = 0

for a in range(3):
    pessoa = {}
    pessoa['idade'] = int(input(f'Idade {a+1}o: '))
    pessoa['altura'] = float(input(f'Altura {a+1}o: '))
    acu_altura+=pessoa['altura']

    lista_pessoas.append(pessoa)

media_altura = acu_altura/len(lista_pessoas)

cont_pess = 0
if pessoa['idade'] > 13:
    if pessoa['altura'] < media_altura:
        cont_pess+=1

print(f'Foram identificadas {cont_pess} pessoas com mais de 13 anos com altura inferior a media {media_altura} anos.')
print(lista_pessoas)


