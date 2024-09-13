num = int(input("insira um número inteiro: "))

if(num > 0):
    if(num % 2) == 0:
        print("número par")
    else:
        print("número ímpar")
else:
    print("número inválido")