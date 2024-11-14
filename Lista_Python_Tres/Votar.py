def verifica_voto(idade):
    if idade < 16:
        return "Não pode votar"
    elif 16 <= idade < 18 or idade > 65:
        return "Voto opcional"
    else:
        return "Voto obrigatório"

idade = int(input("Digite sua idade: "))
print(verifica_voto(idade))
