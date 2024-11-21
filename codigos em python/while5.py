num = 0
alcool = 0
gasolina = 0
diesel = 0
while num!=4:
    num=int(input('Digite o número correspondente ao tipo de combustível que o cliente utilizou: '))
    if num == 1:
        alcool = alcool+1
    if num == 2:
        gasolina = gasolina + 1
    if num == 3:
        diesel = diesel + 1
print(f'Muito obrigado Alcool: {alcool} Gasolina: {gasolina} Diesel: {diesel}')