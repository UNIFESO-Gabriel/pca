def main() -> None:
    """
    PROPOSITOS:
    1- Ler a quantidade de numeros 'n';
    2- Ler 'n' numeros;
    3- Somar os 'n' numeros;
    4- Mostrar a soma dos 'n' numeros.
    """
    # Ler a quantidade de numeros 'n'.
    n: int = int(input("Digite o valor referente a quantidade de numeros 'n': "))
    
    # Ler 'n' numeros.
    if n >= 0:
        lista: list[int] = []
        i: int = 1
        
        while (i <= n):
            num: int = int(input(f"Digite o numero {i}: "))
            lista.append(num)
            i = i + 1
            
        soma1: int = 0
        # Somar os 'n' numeros
        for numero in lista:
            soma1 = soma1 + numero
            
        soma2: int = 0
        for i in range(len(lista)):
            soma2 = soma2 + lista[i - 1]
        
        # Mostrar a soma dos 'n' numeros
        print(soma1, soma2)
        
    else:
        print(f"'n' é negativo: {n}")


if __name__ == "__main__":
    main()