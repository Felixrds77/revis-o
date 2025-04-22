minimo = float(input("digite o salario minimo: "))
while True:
    salario = float(input("digite seu salario: "))
    if salario <=0:
        break
    soma = salario/minimo
    soma2 = salario - minimo
    print(f"você recebe {int(soma)} salarios minimo com um almento de {soma2}")