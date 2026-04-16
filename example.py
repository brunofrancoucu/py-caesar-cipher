import cipher # from cipher import normalize, encrypt, decrypt

plaintext = cipher.normalize("¡Hola, Mundo!")
print(f"plaintext = {plaintext}") # "holamundo"

ciphertext = cipher.encrypt(plaintext)
print(f"ciphertext = {ciphertext}")  # "sfpyqensj"

recovered_plaintext = cipher.decrypt(ciphertext)
print(f"recovered_plaintext = {recovered_plaintext}") # "holamundo"