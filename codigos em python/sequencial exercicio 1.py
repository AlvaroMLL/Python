n1 = int(input('Digite um número inteiro e positivo: '))
if n1 >= 0:
    if n1 % 2 == 0:
        print(f'{n1} é par')
    else:
     print(f'{n1} é impar')     
else:
    print(f'Informe um valor positivo')
