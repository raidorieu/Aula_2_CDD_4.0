#média do aluno
n1=float(input("qual foi a primeira nota do aluno? "))
n2=float(input("qual foi a segunda nota do aluno? "))
n3=float(input("qual foi a teceira nota do aluno? "))
m=(n1+n2+n3)/3
if (n1>=0 and n1 <=10) or (n2>=0 and n2<=10) or (n3>=0 and n3<=10):
    print(f"a média do aluno é {m:.2f}")
    if m>=7 and m<=10:
        print("o aluno está aprovado")
    else:
        if m<7 and m>=4:
            print("o aluno está de recuperação")
        else:
            print("o aluno está reprovado")
else:
    print("notas invalidas")
