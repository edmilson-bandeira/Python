n = int(input("insere o total de notas: "))
notas = []

controller = 0

while controller <= n :
    nota = int(input("insere a nota: "))
    if (nota < 0 or nota > 20):
        print("nota inválida :(")
    else: 
        notas.append(nota)
        media = sum(notas) / len(notas)
        print("média: " + str(media))
    controller+=1

