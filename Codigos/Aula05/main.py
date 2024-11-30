MAX = 100

def soma_for() -> int:
    soma: int = 0
    
    for numero in range(0, MAX + 1):
        soma = soma + numero
            
    return soma

def soma_for_break() -> int:
    soma: int = 0
    
    for numero in range(0, MAX + 1):
        if numero == 50:
            break
        
        soma = soma + numero        
            
    return soma


def soma_for_continue() -> int:
    soma: int = 0
    
    for numero in range(0, MAX + 1):
        if numero == 50:
            continue
        
        soma = soma + numero        
            
    return soma


def soma_while() -> int:
    i: int = 0 # variável contadora.
    soma: int = 0
    
    while i <= MAX:
        soma = soma + i
        i = i + 1 # contando mais 1.
    
    return soma


def leitura_teclado(letra: str) -> None:
    while letra != 'e':
        letra = input("Digite uma letra ('e' para sair): ")


def main() -> None:
    resultado = soma_for_continue()
    print(f"Soma (continue): {resultado}.")
    resultado = soma_for_break()
    print(f"Soma (break): {resultado}.")
    
if __name__ == "__main__":
    main()