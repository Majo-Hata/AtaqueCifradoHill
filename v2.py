import numpy as np

def matriz_inversa_modulo(matriz, modulo):
    det = int(round(np.linalg.det(matriz)))
    adjunta = np.round(np.linalg.inv(matriz) * det)
    inversa = np.mod(adjunta, modulo)
    return inversa

def obtener_clave_descifrado(mensaje_claro, texto_cifrado):
    n = int(len(texto_cifrado) ** 0.5)
    mensaje_claro = mensaje_claro.replace(" ", "").upper()
    mensaje_claro = [ord(char) - 65 for char in mensaje_claro]
    texto_cifrado = texto_cifrado.replace(" ", "").upper()
    texto_cifrado = [ord(char) - 65 for char in texto_cifrado]

    # Agregar caracteres de relleno a texto_cifrado si es necesario
    while len(mensaje_claro) % n != 0:
        mensaje_claro.append(23)  # Agregar 'W' como relleno
        texto_cifrado.append(23)  # Agregar 'W' como relleno

    matriz_mensaje = np.array(mensaje_claro).reshape(-1, n)
    matriz_cifrado = np.array(texto_cifrado).reshape(-1, n)
    
    matriz_clave = np.dot(matriz_mensaje, matriz_inversa_modulo(matriz_cifrado, 26)) % 26
    clave = "".join([chr(x + 65) for x in matriz_clave.flatten()])
    return clave

# Ejemplo de uso
if __name__ == "__main__":
    mensaje_claro = "HELLO"
    texto_cifrado = "PWFNF"

    clave_descifrado = obtener_clave_descifrado(mensaje_claro, texto_cifrado)
    print("Clave de descifrado:", clave_descifrado)
