'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes 
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o 
usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos 
e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e 
dos pesos dos clientes'''

'''

peso_menor = peso_maior = altura_menor = altura_maior = codigo_menor_altura = cogigo_maior_altura = \
    codigo_menor_peso = codigo_maior_peso = None

while True:
    codigo = int(input('Codigo: '))
    if codigo == 0:
        break
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))

    if altura_menor is None or altura < altura_menor:
        altura_menor = altura
        codigo_menor_altura = codigo

    if altura_maior is None or altura > altura_maior:
        altura_maior = altura
        cogigo_maior_altura = codigo

    if peso_menor is None or peso < peso_menor:
        peso_menor = peso
        codigo_menor_peso = codigo

    if peso_maior is None or peso > peso_maior:
        peso_maior = peso
        cogigo_maior_peso = codigo

print(f'maior altura {altura_maior} - codigo {cogigo_maior_altura}')
print(f'menor altura {altura_menor} - codigo {codigo_menor_altura}')
print(f'maior peso {peso_maior} - codigo {cogigo_maior_peso}')
print(f'menor peso {peso_menor} - codigo {codigo_menor_peso}')
'''
peso_menor = peso_maior = altura_menor = altura_maior = codigo_menor_altura = cogigo_maior_altura = \
    codigo_menor_peso = codigo_maior_peso = None

cadastro = []

while True:
    codigo = int(input('Codigo: '))
    if codigo == 0:
        break
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))

    pessoa = [codigo,altura,peso]

    cadastro.append(pessoa)

    if altura_menor is None or pessoa[1] < altura_menor:
        altura_menor = pessoa[1]
        codigo_menor_altura = codigo

    if altura_maior is None or pessoa[1] > altura_maior:
        altura_maior = pessoa[1]
        cogigo_maior_altura = codigo

    if peso_menor is None or pessoa[2] < peso_menor:
        peso_menor = pessoa[2]
        codigo_menor_peso = codigo

    if peso_maior is None or pessoa[2] > peso_maior:
        peso_maior = pessoa[2]
        cogigo_maior_peso = codigo

print(f'maior altura {altura_maior} - codigo {cogigo_maior_altura}')
print(f'menor altura {altura_menor} - codigo {codigo_menor_altura}')
print(f'maior peso {peso_maior} - codigo {cogigo_maior_peso}')
print(f'menor peso {peso_menor} - codigo {codigo_menor_peso}')












