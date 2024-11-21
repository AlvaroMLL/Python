idademaior = idademenor = 0
#jeito de economizar linhas
idade_maior = -1 
idade_menor = 200 
for i in range(6):
    idades = int(input('Digite aqui sua idade: '))
    if idades > idade_maior:
        idade_maior = idades
    if idades < idade_menor:
        idade_menor = idades

print(f'O mais velho tem {idade_maior} anos.')
print(f'O mais novo tem {idade_menor} anos.')




