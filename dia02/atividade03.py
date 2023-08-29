# Crie um programa e diga um nuero que mostre o sucessor e o antecessor
numero = int(input("Digie seu numero: "))

num = input("Qual numero deseja") # retornar uma string digitada pelo user

sucessor = 0
antecessor = 0

try:
    recebaSucesso = numero + 1
    recebaAntecessor = numero -1
except ValueError:
        raise ValueError("Digite um numero valido")
        
        

print(f"Esse é o sucessor do seu numero: {recebaSucesso}")
print(f"Esse é o antecessor do seu numero: {recebaAntecessor}")


