def calcular_desconto(valor_compra, tipo_cliente, cupom):
    """Calcula o valor final com desconto."""
    if valor_compra <= 0:
        return 0

    if tipo_cliente == "premium":
        desconto = 0.15
    elif tipo_cliente == "regular":
        desconto = 0.05
    else:
        desconto = 0

    if cupom == "DESC10" and valor_compra > 100:
        desconto += 0.10

    valor_final = valor_compra * (1 - desconto)

    if valor_final < 50:
        valor_final += 5  # taxa mínima de entrega

    return round(valor_final, 2)
