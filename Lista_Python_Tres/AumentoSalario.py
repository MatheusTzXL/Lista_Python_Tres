def aumento_salario(salario):
    return salario * 1.25

salario = float(input("Digite o salário atual: "))
novo_salario = aumento_salario(salario)
print(f"O salário com aumento de 25% é: R${novo_salario:.2f}")
