print(" a " * 10)



num = input("Digite sua idade: ")

try:
    if (int(num) >= 10):
        print("Voce possui idade certa")
    else:
      print("Diga apenas sua idade para validar se ela esta correta: ")

except ValueError:
    raise ValueError("Digite o valor do numero valido")

if idade_em_int >= 18:
    print("Pode tirar a CNH")
else:
    print("Não pode tirar a CNH")