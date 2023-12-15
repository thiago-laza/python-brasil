'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, 
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas 
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''



meses = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
meses_temperaturas = {}
acu_temp = 0

for t in range(len(meses)):
    meses_temperaturas[f'{meses[t]}'] = float(input(f'Temperatura {meses[t]}: '))
    acu_temp+=meses_temperaturas[f'{meses[t]}']

media_temperaturas = acu_temp/len(meses)

for j,k in meses_temperaturas.items():
    if k > media_temperaturas:
        print(f'O mes de {j} teve media de temperatura de {k}⁰C ficando acima da media anual que foi de {media_temperaturas:.2f}⁰C')





