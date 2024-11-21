cont=0
for x in range(8):
    nota = int(input('Digite uma nota: '))
    if nota >= 0 and nota <= 100:
        cont=cont+1
print(f'Foram informadas {cont} notas válidas para o Suap.')
