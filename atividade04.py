# Checar e transformar em int
velocidade_em_int = 0
velocidade = input("Digite a velocidade (em km): ")

try: 
      velocidade_em_int = int(velocidade)
except ValueError:
    raise ValueError("Digite um numero: ")

if velocidade_em_int > 80:
     print(f"velocidade acima do limite {velocidade_em_int}")
     print(f"Multa de: {(velocidade_em_int - 80) * 7}")
elif velocidade_em_int == 80:
     print(f"Atigindo velocidade limite")
else: 
     print(f"Velocidade abaixo do limite. parabens")

