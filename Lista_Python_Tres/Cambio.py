def converter_real_para_dolar(valor_em_reais, taxa_de_cambio):
    return valor_em_reais / taxa_de_cambio

valor_em_reais = float(input("Digite o valor em reais (R$): "))
taxa_de_cambio = float(input("Digite a taxa de câmbio atual (1 USD em BRL): "))
valor_em_dolar = converter_real_para_dolar(valor_em_reais, taxa_de_cambio)
print(f"O valor em dólares é: ${valor_em_dolar:.2f}")

