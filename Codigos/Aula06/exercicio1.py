"""
Escreva um programa em que leia uma sequência de números e exiba a soma deles.
"""


TAMANHO = 5

def ler_numeros() -> list[int]:
    numeros: list[int] = []
    
    for i in range(TAMANHO):
        numero: int = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
        
    return numeros
    

def somar_numeros(numeros: list[int]) -> int:
    return sum(numeros)


def main() -> None:
    numeros: list[int] = ler_numeros()
    soma: int = somar_numeros(numeros)
    print(f"A soma dos números é: {soma}")
    
    
if __name__ == "__main__":
    main()