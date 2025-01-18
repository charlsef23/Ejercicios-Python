"""
Pide un voto entre A y B y manipula los resultados para que B gane siempre
"""
res = {"A": 10, "B": 10}

voto = input("A o B? ").upper()

res [voto] += 1
res ["B"] += 5

print(res)