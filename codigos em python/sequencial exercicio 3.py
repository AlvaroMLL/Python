nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
idade1 = int(input('Informe a idade da primeira pessoa: '))
idade2 = int(input('Informe a idade da segunda pessoa: '))

if idade1 != idade2:
    if idade1 > idade2:
        print(f'{nome1} é mais velho do que {nome2}')
    else:
        print(f'{nome2} é mais velho do que {nome1}')
else:
    print('Eles tem a mesma idade')

    
