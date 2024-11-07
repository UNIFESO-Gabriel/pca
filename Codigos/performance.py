from time import perf_counter
from itertools import chain

lista1 = list(range(0, 50_000_000))
lista2 = list(range(50_000_001, 100_000_001))

inicio = perf_counter()

# for numero in lista2:
#     lista1.append(numero)

# lista = lista1 + lista2

lista = list(chain(lista1, lista2))

fim = perf_counter()

print(f"Lista tem {len(lista1):,} elementos.")
print(f"Tempo de execução: {fim - inicio} segundos.")