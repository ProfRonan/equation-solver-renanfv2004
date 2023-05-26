import math

def equacao():
    grau = float(input("Digite o grau da equação: "))

    if grau < 1 or grau > 2:
        print("Grau inválido")
    elif grau == 1:
        a = float(input("Digite o valor de a: "))
        if a == 0:
            print("Valor de a inválido")
        else:
            b = float(input("Digite o valor de b: "))
            x = -b / a
            print(f"O valor da raiz é: {x:.2f}")
    elif grau == 2:
        a = float(input("Digite o valor de a: "))
        if a == 0:
            print("Valor de a inválido")
        else:
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            delta = b**2 - 4*a*c
            if delta < 0:
                print("A equação não possui raízes reais")
            elif delta == 0:
                x = -b / (2*a)
                print(f"A equação possui uma raiz real: {x:.2f}")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                print(f"A equação possui duas raízes reais: {x1:.2f} e {x2:.2f}")
    else:
        print("Grau inválido")

equacao()

