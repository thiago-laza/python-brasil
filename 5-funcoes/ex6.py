'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre 
a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar 
as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que 
permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.'''

def conversao(h):
    if hora >=13 and hora < 24:
        nova_h = hora - 12
        print(f'{nova_h}:{minutos} P.M')
    else:
        print(f'{hora}:{minutos} A.M')





while True:
    hora = int(input('Hora: '))
    while hora < 0 or hora > 24:
        hora = int(input('Informe um valor valido para a hora: '))
    minutos = int(input('Minutos: '))
    while minutos < 0 or minutos > 59:
        minutos = int(input('Informe um valor valido para os minutos: '))
    conversao(hora)
    resp = input('Deseja converter mais alguam hora? [s/n]: ')
    if resp == 'n':
        break