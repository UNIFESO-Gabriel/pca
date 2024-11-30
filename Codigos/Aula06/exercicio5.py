"""
Faça um programa que conte o número de vogais e consoantes em uma string fornecida pelo
usuário.
"""
import string
from collections import Counter

def ler_entrada() -> str:
    return input("Digite uma string qualquer: ")


def contar_numero_vogais_consoantes(entrada: str) -> tuple[int, int]:
    entrada = entrada.lower()
    vogais: set[str] = {'a', 'e', 'i', 'o', 'u'}
    consoantes: set[str] = set(string.ascii_lowercase) - vogais
    
    contador = dict(Counter(entrada))
    
    total_vogais = \
        sum(map(lambda key: contador.get(key, 0) if key in vogais else 0, contador.keys()))
        
    total_consoantes = sum(\
        map(lambda key: contador.get(key, 0) if key in consoantes else 0, contador.keys()))   
    
    return total_vogais, total_consoantes


def main() -> None:
    
    entrada = ler_entrada()
    
    qtd_vogais, qtd_consoantes = \
        contar_numero_vogais_consoantes(entrada)
        
    print(f"{entrada} possui:\n{qtd_vogais} vogais;\n{qtd_consoantes} consoantes.")
    
    
if __name__ == '__main__':
    main()