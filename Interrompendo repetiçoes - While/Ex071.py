print('=' * 30)
print('{:^30}'.format('BANCO RAUL'))
print('=' * 30)
valor = int(input('Que valor voce quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print(f'O total de {totced} de {ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Obrigado por passar no BANCO RAUL! Volte sempre.')

