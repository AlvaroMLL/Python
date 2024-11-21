n=int(input('Primeiro inteiro: '))
x=int(input('Segundo número inteiro: '))
y=int(input('Terceiro número inteiro: '))
cont=0
for z in range(x,y+1):
    if z%n==0:
        cont=cont+1
print(f'{cont}')
        