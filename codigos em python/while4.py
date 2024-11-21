nota1 = float(input('Digite a primeira nota: '))
while nota1<0 or nota1>10:
        print('Nota inválida')
        nota1 = float(input('Digite a primeira nota: '))
        
nota2 = float(input('Digite a segunda nota: '))
while nota2 < 0 or nota2 > 10:
    print('Nota inválida')
    nota2 = float(input('Digite a segunda nota: '))
total = nota1 + nota2
media = total / 2
print(f'Média = {media:.2f}')
 