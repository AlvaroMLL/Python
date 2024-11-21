votossim=0
votosnao=0
votosinvalidos=0
total = 80
for i in range(80):
    votos = (input('Digite aqui seu voto SIM ou NAO: '))
    if votos == 'SIM':
        votossim=votossim + 1
    elif votos == 'NAO':
        votosnao=votosnao + 1
    else:
        votosinvalidos= votosinvalidos + 1
    porcentvotossim = votossim/total *100
    porcentvotosnao = votosnao/total *100
    porcentvotosinv = votosinvalidos/total *100
print(f"Porcentagem de votos SIM: {porcentvotossim:.1f}%") 
print(f"Porcentagem de votos NAO: {porcentvotosnao:.1f}%")
print(f"Porcentagem de votos inválidos: {porcentvotosinv:.1f}%") 
