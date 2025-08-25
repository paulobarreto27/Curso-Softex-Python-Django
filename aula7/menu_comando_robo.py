posicao_inicial = 0
avancar = 1
recuar = 2
status = 3
desligar = 4

while True:
    print(f"Digite um comando desejado")
    escolha = int(input(f"o que você quer que o Robô faça): {1, 2, 3, 4}. "))
    if escolha == 1:
        print("O robô anda para frente")
        posicao_inicial += 1
    elif escolha == 2:
        print("O robô anda para trás")
        posicao_inicial -= 1
    elif escolha == 3:
        print("O robô mostra o status")
        print(posicao_inicial) 
    elif escolha == 4:
        print("O robô irá desligar")
        break 
    else: 
        print(f"Comando inválido")
        