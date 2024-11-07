"""
Escreva um programa que leia uma lista de números inteiros e exiba-os em ordem crescente;
"""

from random import randint

TAMANHO = 10


def ler_numeros() -> list[int]:
    
    # simulando a leitura de TAMANHO números.
    return [randint(1, 100) for i in range(TAMANHO)]
        
    

def bubble_sort(lista: list[int]) -> list[int]:
    
    for i in range(TAMANHO - 1):
        for j in range(TAMANHO - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista



def main() -> None:
    lista: list[int] = ler_numeros()
    print(f"Lista original: {lista}")
    lista_ordenada = bubble_sort(lista)
    print(f"Lista ordenada (bubble sort): {lista_ordenada}")
    print(f"Lista ordenada com built-in functions: {sorted(lista)}")
    
    
if __name__ == "__main__":
    main()