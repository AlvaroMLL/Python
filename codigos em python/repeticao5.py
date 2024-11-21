cont=0
for x in range (6):
    m1 = int(input('Primeiro lado: '))
    m2 = int(input('Segundo lado: '))
    m3 = int(input('Terceiro lado: '))
    if m1+m2>m3 and m2+m3>m1 and m1+m3>m2:
        cont=cont+1    
print(f'Quantidade de piramides: {cont}') 