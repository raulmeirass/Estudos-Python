while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 20)
    if tab < 0:
        break
    for c in range (1, 11):
        print(f'{tab} x {c} = {tab * c}')
    print('--' * 20)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')