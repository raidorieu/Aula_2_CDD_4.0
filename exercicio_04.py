#試合
casa=input("qual é o nome do time da casa? ")
visitante=input("qual é o nome do time visitante? ")
golc=int(input(f"quantos gols o {casa} fez? "))
golv=int(input(f"quantos gols o {visitante} fez? "))
if golc==golv:
    print("empate")
else:
    if golc>golv:
        print(f"{casa} venceu")
    else:
        print(f"{visitante} venceu")
