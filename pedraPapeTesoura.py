from random import choice
from time import sleep
list = ['PEDRA','PAPEL','TESOURA']
print('VAMOS JOGAR PEDRA, PAPEL OU TESOURA ?! ')
print('-='*20)
contadorEu = contadorPc = contadorEmpate =0
while True:
    pc = choice(list)
    eu = ''
    while eu not in list:
        eu = str(input('Digite PEDRA, PAPEL OU TESOURA para jogar: ')).strip().upper()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    if pc == eu :
        contadorEmpate += 1
        print(f'O computador escolheu {pc} e voce {eu}, então voces EMPATARAM')
    elif pc == 'PEDRA' and eu == 'PAPEL':
        contadorEu += 1
        print(f'O computador escolheu {pc} e você {eu}, então VOCE VENCEU!!!')
    elif pc == 'PAPEL' and eu == 'PEDRA':
        contadorPc += 1
        print(f'O computador escolheu {pc} e você {eu} então o COMPUTADOR VENCEU')
    elif pc == 'TESOURA' and eu == 'PEDRA':
        contadorEu += 1
        print(f'O computador escolheu {pc} e voce {eu} então VOCÊ VENCEU!!!')
    elif pc == 'PEDRA' and eu == 'TESOURA':
        contadorPc += 1
        print(f'O computador escolheu {pc} e você {eu} então O COMPUTADOR VENCEU!!!')
    elif pc == 'PAPEL' and eu == 'TESOURA':
        contadorEu += 1
        print(f'O compoutador escolheu {pc} e você {eu} então VOCÊ VENCEU')
    elif pc == 'TESOURA' and eu == 'PAPEL':
        contadorPc += 1
        print(f'O computador escolheu {pc} e você {eu} então o COMPUTADOR VENCEU!!!')
    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Quer jogar novamente? [S/N]: ')).strip().upper()[0]
    if decisao == 'N':
        break


print('=-' * 20)
print('Relatorio final')
print('=-' *20)
print(f'Vitorias Computador: {contadorPc} \nVitorias Você: {contadorEu} \nEmpates: {contadorEmpate}')
print('Obrigado por jogar! TENHA UM BOM DIA!')
