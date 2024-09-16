n = int(input("insere o total de notas: "))
notas = []
media = 0

controller = 1

while controller <= n :
    nota = int(input("insere a nota: "))
    if (nota < 0 or nota > 20):
        print("nota inválida :(")
        controller = 0
    else: 
        notas.append(nota)
        media = sum(notas) / len(notas)
        round(media, 2)
    controller+=1   

print("média: " + str(media))



