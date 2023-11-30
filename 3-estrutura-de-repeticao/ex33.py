'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto 
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média 
das temperaturas.'''

numero_temperaturas = int(input('Informe quantas temperaturas serao digitadas: '))


primeira_temperatura = float(input('Informe a 1⁰ temperatura: '))

menor_temperatura = primeira_temperatura
maior_temperatura = primeira_temperatura
acumulador = primeira_temperatura

cont = 0

while cont < numero_temperaturas - 1:
    temperatura = float(input(f'Informe a {cont+2}⁰ temperatura: '))

    acumulador += temperatura

    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

    elif temperatura < menor_temperatura:
        menor_temperatura = temperatura

    cont+=1

    media = acumulador/(cont+1)

print(f'Foram informadas {numero_temperaturas} temperaturas.')
print(f'A menor temperatura foi {menor_temperatura} ⁰C')
print(f'A maior temperatura foi {maior_temperatura} ⁰C')
print(f'A media das temperaturas foi de {media} ⁰C')


