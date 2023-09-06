#combustível
tipo=input("informe o tipo de combustível: ")
quantidade=float(input("quantos litros foi abastercido: "))
total=0
if tipo== "g":
    total=quantidade*5.8
else:
    total=quantidade=4.9

print(f"você gastou {total}")