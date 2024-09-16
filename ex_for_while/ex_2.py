import random

num_Alet = random.randint(1, 50)

max_tentativas = 5
tent_restantes = max_tentativas

print("adivinha o numero")

while tent_restantes > 0:
    palpite = int(input("Digite o seu palpite: "))
    if palpite == num_Alet:
        print("Parabés! Acertaste o número secreto")
        break
    elif palpite < num_Alet:
         print("O número secreto é maior.")
    else: 
        palpite > num_Alet
        print("O número secreto é menor.")

    tent_restantes -= 1
    print("Tentativas restantes: " + str(tent_restantes))