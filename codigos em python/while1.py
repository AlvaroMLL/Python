x = 0
y = 1
while (x != y):
    x = int(input('Digite um valor para x: '))
    y = int(input('Digite um valor para y: '))
    if x > y:
        print('Decrescente')
    #if x < y:
    else:
        print('Crescente')
print('Fim')