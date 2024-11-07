from math import gcd


class Fracao:
    
    # método construtor
    def __init__(self, numerador: int, denominador: int) -> None:
        if denominador == 0:
            raise ValueError('Denominador não pode ser zero.')
        
        self.numerador: int = numerador
        self.denominador: int = denominador
    
    def transformar_decimal(self) -> float:
        return self.numerador / self.denominador
    
    def __str__(self) -> str:
        return f'{self.numerador}/{self.denominador}'
    
    def __mul__(self, other: 'Fracao') -> 'Fracao':
        """Multiplicação de frações usando *"""
        resultado = Fracao(self.numerador * other.numerador,
                         self.denominador * other.denominador)
        return self._simplificar(resultado)
    
    def __truediv__(self, other: 'Fracao') -> 'Fracao':
        """Divisão de frações usando /"""
        resultado = Fracao(self.numerador * other.denominador,
                         self.denominador * other.numerador)
        return self._simplificar(resultado)
    
    def __add__(self, other: 'Fracao') -> 'Fracao':
        """Adição de frações usando +"""
        resultado = Fracao(self.numerador * other.denominador + other.numerador * self.denominador,
                         self.denominador * other.denominador)
        return self._simplificar(resultado)
    
    def __sub__(self, other: 'Fracao') -> 'Fracao':
        """Subtração de frações usando -"""
        resultado = Fracao(self.numerador * other.denominador - other.numerador * self.denominador,
                         self.denominador * other.denominador)
        return self._simplificar(resultado)
    
    def _simplificar(self, fracao: 'Fracao') -> 'Fracao':
        # calculo o MDC (Máximo Divisor Comum) entre o numerador e o denominador
        mdc: int = gcd(fracao.numerador, fracao.denominador)
        
        # crio uma nova fração simplificada
        frac_simplificada: Fracao = \
            Fracao(fracao.numerador // mdc, fracao.denominador // mdc)
            
        return frac_simplificada