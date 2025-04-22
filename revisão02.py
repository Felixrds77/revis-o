a = float(input("digite um numero para saber se ele é par ou impar, negativo ou pisitivo: "))
if a>=0:
    if a%2==0:
        print("o numero é par e positivo")
    else:
        print("o numero é impar e positivo")
else:
    if a%2==0:
        print("o numero é par e negativo")
    else:
        print("o numero é impar e negativo")