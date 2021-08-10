import numpy as np

# Arreglos que simulan matrices ----------------------------
a = np.array([[1,2], [3,4]])

print(a + a)

# Matrices de verdad ---------------------------------------
m = np.matrix([[5,7],[8,9]])

print(m + m)

# Sumando arreglos y matrices ------------------------------
print(a + m)

# Producto de un escalar por una matriz -------------------
print(2 * a)

# Multiplicando matrices --------------------------------
print(a @ m)

# Matriz transpuesta -----------------------------------
print(m.T)

# Determinante de una matriz ---------------------------
determinante = np.linalg.det(a)
print(determinante)

# Inversa de una matriz --------------------------------
inversa = np.linalg.inv(a)
print(inversa)

identidad = a @ inversa

print(identidad)
