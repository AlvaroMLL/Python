x = 1
y = 1
while (x and y != 0):
    x = int(input('Digite a coordenada x: '))
    y = int(input('Digite a coordenada y: '))
    if x > 0 and y > 0:
        print('Primeiro quadrante')
    if x > 0 and y < 0:
        print('Quarto quadrante')
    if x < 0 and y > 0:
        print('Segundo quadrante')
    if x < 0 and y < 0:
        print('Terceiro quadrante')
