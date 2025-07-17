def decimal_para_romano(decimal):
    if decimal <= 0:
        return "N/A" 

    numeros = [ 
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'),  (90, 'XC'), (50, 'L'),  (40, 'XL'),
        (10, 'X'),   (9, 'IX'),  (5, 'V'),   (4, 'IV'),
        (1, 'I')
    ]

    romano = "" 
    for valor, simbolo in numeros: 
        while decimal >= valor: 
            romano += simbolo
            decimal -= valor
    return romano 

numero = int(input("Digite um número decimal: "))
romano = decimal_para_romano(numero)
print(f"O número {numero} em romano é: {romano}")
