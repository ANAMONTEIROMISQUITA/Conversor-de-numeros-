def decimal_para_binario(decimal):
    if decimal == 0: 
        return "0"
    binario = "" 
    while decimal > 0: 
        resto = decimal % 2 
        binario = str(resto) + binario 
        decimal = decimal // 2 
    return binario 

numero = int(input("Digite um número decimal: "))
binario = decimal_para_binario(numero)
print(f"O número {numero} em binário é: {binario}")


