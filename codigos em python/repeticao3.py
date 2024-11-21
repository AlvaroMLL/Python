n=int(input('Qual valor vc quer conhecer os mútiplos? '))
x=int(input('A partir de qual faixa? '))
y=int(input('Até qual valor? '))
for z in range(x,y+1):
    if z%n==0:
        print(f'{z} ',end='')
        
