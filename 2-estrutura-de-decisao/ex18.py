'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

print('Informe uma data no formato dd/mm/aaaa para saber se e uma data valida.')
dia = int(input('Informe do dia: '))
mes = int(input('Informe o mes: '))
ano = int(input('Informe o ano: '))






if mes < 1 or mes > 12:
    print(f'{dia}/{mes}/{ano} e uma data invalida.')
else:
    if mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia < 1 or dia > 29:
                print(f'{dia}/{mes}/{ano} e uma data invalida.')
        else:
            if dia < 1 or dia > 28:
                print(f'{dia}/{mes}/{ano} e uma data invalida.')
            else:
                print(f'{dia}/{mes}/{ano} e uma data valida.')
    elif mes >= 1 and mes <=7 and mes % 2 == 0:
        if dia < 1 or  dia >30:
            print(f'{dia}/{mes}/{ano} e uma data invalida.')
        else:
            print(f'{dia}/{mes}/{ano} e uma data valida.')
    elif mes >=1 and mes <= 7 and mes % 2 != 2:
        if dia < 1 or dia > 31:
            print(f'{dia}/{mes}/{ano} e uma data invalida.')
        else:
            print(f'{dia}/{mes}/{ano} e uma data valida.')
    elif mes > 7 and mes <=12 and mes % 2 == 0:
        if dia < 1 or dia > 31:
            print(f'{dia}/{mes}/{ano} e uma data invalida.')
        else:
            print(f'{dia}/{mes}/{ano} e uma data valida.')
    elif mes > 7 and mes <= 12 and mes % 2 != 0:
        if dia < 1 or dia > 30:
            print(f'{dia}/{mes}/{ano} e uma data invalida.')
        else:
            print(f'{dia}/{mes}/{ano} e uma data valida.')
    
   
