compratotal = 0
cashbacktotal = 0
for x in range (400):
    compra = float(input('Digite o valor da compra: R$'))
    if compra <= 100:
        cashback = compra * 0.04
    elif compra <=200:
        cashback = compra * 0.06
    elif compra <=400:
        cashback = compra * 0.08
    elif compra >400:
        cashback = compra * 0.1
    compratotal = compratotal + compra
    cashbacktotal = cashbacktotal + cashback
print(f'Valor total das compras é: R${compratotal:.2f}')
print(f'O valor total de cashback é: R${cashbacktotal:.2f}')

