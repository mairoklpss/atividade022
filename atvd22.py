# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
contador = 0

while True:
    numero = int(input("Digite os números que desejas somar (digite 0 quando quiser parar): "))
    if numero == 0:
        break
    contador += numero
    
print(f"a soma dos números digitado é:", contador)