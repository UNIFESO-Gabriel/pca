from sys import stderr
from fracao import Fracao


def main() -> None:
    
    # 'fracao1' e 'fracao2' são OBJETOS da CLASSE Fracao.
    try:
        fracao1: Fracao = Fracao(2, 3)
        fracao2: Fracao = Fracao(27, 0)
        
        resultado = fracao1 - fracao2
        
        print(f'O resultado da multiplicação de {fracao1} por {fracao2} é: {resultado} e em decimal é: {resultado.transformar_decimal():.5f}')
    
    except ValueError as e:
        print(f'Erro de divisão por zero: {e}', file=stderr)
        
    except Exception as e:
        print(f'Um erro inesperado ocorreu: {e}', file=stderr)


if __name__ == '__main__':
    main()