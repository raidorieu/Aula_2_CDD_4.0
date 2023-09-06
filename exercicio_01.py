#ordem dos números
n1=float(input("digite um número: "))
print(n1)
n2=float(input("digite um segundo número: "))
print(n2)

if n1==n2:
    print("os número são iguais")
else:
    if n1<n2:
        print(n1, n2)
    else:
        print(n2, n1)
