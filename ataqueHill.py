import numpy as np

# Definimos la matriz de texto cifrado
ciphertext = np.array([[4, 13, 21, 23, 22, 24], [13, 11, 21, 8, 3, 17], [6, 0, 18, 3, 3, 15], [3, 4, 11, 8, 20, 17], [0, 12, 0, 9, 6, 15], [13, 2, 7, 6, 9, 8], [0, 3, 4, 25, 12, 6], [2, 21, 25, 5, 22, 25], [15, 13, 15, 21, 14, 20]])

# Definimos la matriz de vectores unitarios
unit_vectors = np.zeros((9, 3))
unit_vectors[0] = [1, 0, 0]

# Realizamos las operaciones lineales para obtener los vectores unitarios
for i in range(1, 9):
    factor = np.linalg.inv(ciphertext[0:2, 0:2]) @ ciphertext[i, 0:2] % 27
    unit_vectors[i] = np.concatenate((factor, [0]))

# Comprobamos si los vectores unitarios son linealmente independientes
if np.linalg.matrix_rank(unit_vectors) < 3:
    print("Los vectores unitarios no son linealmente independientes.")
else:
    # Calculamos la inversa de la matriz de vectores unitarios
    inv_unit_vectors = np.linalg.pinv(unit_vectors)

    # Restamos las filas de la matriz de texto cifrado para obtener el mensaje en claro
    decrypted_message = (ciphertext @ inv_unit_vectors) % 27

    # Convertimos los números en letras
    plaintext = ''
    for i in range(9):
        for j in range(6):
            plaintext += chr(decrypted_message[i, j] + 65)

    print(plaintext)