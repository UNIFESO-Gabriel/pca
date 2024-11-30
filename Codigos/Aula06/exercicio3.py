"""
Escreva um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador
tenta adivinhar. O programa deve dar dicas se o palpite é muito alto ou muito baixo e contar o
número de tentativas.
"""
from random import randint

LIMITE_INFERIOR = 1
LIMITE_SUPERIOR = 10

def sortear_numero() -> int:
    return randint(LIMITE_INFERIOR, LIMITE_SUPERIOR)


def escolher_numero() -> int:
    numero_escolhido = int(input("Digite um número para adivinhar: "))
    
    if numero_escolhido < LIMITE_INFERIOR or numero_escolhido > LIMITE_SUPERIOR:
        raise ValueError(f"Número escolhido {numero_escolhido} não está entre {LIMITE_INFERIOR} e {LIMITE_SUPERIOR}.")
    
    return numero_escolhido


def verificar_escolha(numero_sorteado: int, numero_escolhido: int) -> bool:
    
    resposta: bool = False
    
    if numero_escolhido == numero_sorteado:
        print("Você adivinhou o número!")
        resposta = True
    elif numero_escolhido < numero_sorteado:
        print("Chute acima do número sorteado...")
    else:
        print("Chute abaixo do número sorteado...")
    
    return resposta


def main() -> None:
    
    max_tentativas: int = int(input("Digite o número máximo de tentativas: "))
    numero_sorteado = sortear_numero()
    tentativas: int = 0
    
    for i in range(max_tentativas):
        numero_escolhido: int = int(input(f"Digite um número (tentativa {i+1}): "))
        
        if not verificar_escolha(numero_sorteado, numero_escolhido):
            tentativas += 1
        else:
            break
            
    if tentativas == max_tentativas:
        print(f"Você atingiu o número máximo de tentativas e não adivinhou o número {numero_sorteado}.")
    else:
        print(f"Você adivinhou o número {numero_sorteado} na {tentativas} tentativa!")
    
    
if __name__ == "__main__":
    main()