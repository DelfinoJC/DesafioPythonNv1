print(f"Digite um número inteiro e te direi se ele é par ou ímpar.")
num = int(input())

def primo ():
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")

if primo():
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")