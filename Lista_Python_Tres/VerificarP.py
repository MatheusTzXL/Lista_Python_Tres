def par_ou_impar(numero):
    return "Par" if numero % 2 == 0 else "Ímpar"

numero = int(input("Digite um número: "))
print(par_ou_impar(numero))
