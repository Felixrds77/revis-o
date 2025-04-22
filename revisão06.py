peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
soma = peso / (altura * altura)
if soma <=18.6:
    print("abaixo do peso")
elif soma >=18.6:
    print("peso ideal parabens")
elif soma >=25.0:
    print("levemente a cima do peso")
elif soma >=30.0:
    print("obesidade grau I")
elif 35.0 <= soma <= 39.9:
    print("obesidade grau II (severa)")
else:
    print("obesidade grau III (morbida)")



