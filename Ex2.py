A = int(input("Valor A "))
B = int(input("Valor B "))
aux = 0

print(f"Antes {A}")
print(f"Antes {B}")

aux = A
A = B
B = aux

print(f"Trocado {A}")
print(f"Trocado {B}")