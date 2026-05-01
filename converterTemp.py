print("Bem-vindo ao conversor de temperatura!")
print("Digite a letra correspondente à temperatura que você quer converter:")
print("C - Celsius")
print("F - Fahrenheit")
print("K - Kelvin")

letra1 = input("Digite a primeira letra da temperatura que você quer converter: ")

letra2 = input("Digite a segunda letra da temperatura que você quer converter: ")

def converterCelsius():
    if letra1 == "C" and letra2 == "F":
        temp = float(input("Digite a temperatura em Celsius: "))
        resultado = (temp * 9/5) + 32
        print(f"{temp}°C é igual a {resultado}°F.")
    elif letra1 == "C" and letra2 == "K":
        temp = float(input("Digite a temperatura em Celsius: "))
        resultado = temp + 273.15
        print(f"{temp}°C é igual a {resultado}K.")
    else:
        print("Conversão inválida para Celsius.")

def converterFahrenheit():
    if letra1 == "F" and letra2 == "C":
        temp = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = (temp - 32) * 5/9
        print(f"{temp}°F é igual a {resultado}°C.")
    elif letra1 == "F" and letra2 == "K":
        temp = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F é igual a {resultado}K.")
    else:
        print("Conversão inválida para Fahrenheit.")

def converterKelvin():
    if letra1 == "K" and letra2 == "C":
        temp = float(input("Digite a temperatura em Kelvin: "))
        resultado = temp - 273.15
        print(f"{temp}K é igual a {resultado}°C.")
    elif letra1 == "K" and letra2 == "F":
        temp = float(input("Digite a temperatura em Kelvin: "))
        resultado = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K é igual a {resultado}°F.")
    else:
        print("Conversão inválida para Kelvin.")

if letra1 == "C":
    converterCelsius()
elif letra1 == "F":
    converterFahrenheit()
elif letra1 == "K":
    converterKelvin()
else:
    print("Letra inválida.")