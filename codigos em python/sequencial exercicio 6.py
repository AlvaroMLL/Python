mes = int(input('Digite o numero de um mês: '))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 10 or mes == 12:
    print(f'O número de dias do mês {mes}  é 31.')

elif mes == 2:
    print(f'O número de dias do mês {mes} é 29, pois 2024 é um ano bissexto.')
    
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print(f'O número de dias do mês {mes} é 30.')
else:
    print('Esse mês não existe')
