def iva_calc(subtotal: float, iva_amount: float) -> float:
    """ Devolvera el valor total con iva"""
    return subtotal * (1 + iva_amount / 100)

producto = "Enchiladas Toks"
precio = 198

precio_total = iva_calc(precio, 16)

print(f"Producto: {producto}")
print(f"Precio sin IVA: ${precio:.2f}")
print(f"Precio con IVA: ${precio_total:.2f}")
