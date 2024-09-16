import random

num_Alet = random.randint(1, 50)

max_tentativas = 5

print("adivinha o numero")
print("Tentativas máxima: " + str(max_tentativas))

while max_tentativas > 0:
    palpite = int(input("Digite o seu palpite: "))
    if palpite == num_Alet:
        print("Parabéns! Acertaste o número secreto! :)")
        break
    elif palpite < num_Alet:
         print("O número secreto é maior.")
    else: 
        palpite > num_Alet
        print("O número secreto é menor.")

    max_tentativas -= 1
    print("Tentativas restantes: " + str(max_tentativas))

print("O jogo terminou!")