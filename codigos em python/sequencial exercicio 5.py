valor_compra= float(input('Digite o valor da compra: R$ '))

if valor_compra <= 100:
    cashback = valor_compra * 0.04
    print(f'Parabéns, você tem direito a R${cashback:.2f} de cashback!')

#elif valor_compra > 100 and valor_compra <= 200:
elif valor_compra <=200:
    cashback = valor_compra * 0.06
    print(f'Parabéns você tem direito a R${cashback:.2f} de cashback!')

#elif valor_compra > 200 and valor_compra <=400:
elif valor_compra <=400:
    cashback = valor_compra * 0.08
    print(f'Parabéns você tem direito a R${cashback:.2f} de cashback!')

#elif valor_compra > 400:
else:
    cashback = valor_compra * 0.1
    print(f'Parabéns você tem direito a R${cashback:.2f} de cashback!')
    
