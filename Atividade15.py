# Crie um progma que rareceba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
def calcular(numero1, numero2, operação):
    if operação == "soma":
        return numero1 + numero2
    elif operação == "subtração":
        return numero1 - numero2
    elif operação == "multiplicação":
        return numero1 * numero2
    elif operação == "divisão":
        if numero2 != 0:
            return "erro:Divisão por zero!"
        else:
            return "Operação inválida!"
        numero1 = float(input("digite o primeiro número:" ))
        numero2 = float(input("Digite o segundo número: "))
        operação = input("Digite a operação(soma, subtração, multiplicação, divisão):").lower()
        resultado = calcular(numero1, numero2, operação)
        print(f"O resultado da operação é: {resultado}")
        
