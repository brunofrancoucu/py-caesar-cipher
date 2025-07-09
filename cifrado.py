"""
Primer trabajo Grupal Programación 1 - Primer semestre 2025
Antonella, Bruno Franco, Diego, Micaela, Tiago

Indice

- Constantes

- Utils
    1 trasladar

- Algoritmos
    1 normalizar
    2 cifrar
    3 decifrar

- Casos de Prueba
"""

'''
Constantes
'''

# abecedario en minuscula
abc = "abcdefghijklmnopqrstuvwxyz"
# abecedario en minuscula acentuado
abcAc = "ábcdéfghíjklmnópqrstúvwxyz"
# abecedario en mayusculas
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# abecedario en mayusculas acentuado
ABCAc = ABC.upper()
# abecedario permutado de a pares (ab <=> ba, cd <==> dc)
bac = "badcfehgjilknmporqtsvuxwzy"

'''
Utils (FunCionEs utilitarias)
'''

'''
1 Trasladar caracteres - usado en algoritmos (2.3) / (3.1)

Entrada, texto -    string con caracteres a ser trasladados dentro del `outSrc`
Entrada, n -        int, cantidad de posiciones a saltar dentro de `outSrc`
Entrada, inSrc -    string con mapeo/caracteres de entrada, usado para obtener posicion
Entrada, outSrc -   string con mapeo/caracteres de salida para misma posicion que los 
                    caracteres en `inSrc` (map de entrada)
Salida -            string con caracteres en `inSrc` de `texto`, trasladados `n` veces en `outSrc` 
                    para primera posicion desde `inSrc`
Descripcion:        Mapear los caracteres de un texto con origen en inSrc a los de `outSrc` (2.1) y 
                    trasladarlos n veces en el `outSrc` (2.2) (cumple con las 2 utilidades, mapeo y traslado)
'''
def trasladar(texto, n = 3, outSrc = abc+abc, inSrc = abc+abc):
    outStr = "" # Texto trasladado / mapeado
    for char in texto:  # asumimos permutado es abc (normalizado)
        inSrcPos = 0  # posicion de char en caracteres de origen `inSrc`
        # 2.1 Mapear indice de inSrc al de outSrc
        for a in inSrc:
            if a == char:
                # 2.2 Trasladar n veces en outSrc
                outStr += outSrc[inSrcPos + n]  # ej. equivalente sin tilde
                break # Evitar duplicados ej outSrc = abc+abc+abc+abc
            inSrcPos += 1
    return outStr

'''
Algoritmos
'''

'''
1 Normalizacion del texto

Entrada, texto -    string
Salida -            string `texto` normalizado (lowC, !acentuado, solo abc)
Descripcion:        Transform `texto` para cada letra verificar modificar o saltear. Convirtiendo a 
                    minusculas, eliminar tildes / acentuaciones, eliminacion de caracteres fuera del alfabeto
'''
def normalizar(texto):
    # Mapeo (mayusculas minusculas y con acentos) a abc desde abcAc+abc+ABC+ABCAc
    return trasladar(texto, 0, abc+abc+abc+abc, abcAc+abc+ABC+ABCAc)

'''
2 Cifrado de un texto normalizado

Entrada, norTxt -   string de un texto normalizado (lowC, !acentuado, solo abc)
Entrada, transN -   int, posiciones a desplazar dentro del alfabeto
Salida -            string, texto cifrado
Descripcion -       Secuencia para cifrado: Invertir orden del texto (2.1), Permutar caracteres (2.2), 
                    Transformar caracteres trsladandolos en el abecedario (2.3)
'''
def cifrar(norTxt, transN = 3):
    # 2.3. Trasladar caracteres n veces (2.2 Permutar caracteres (2.1 Invertir Orden))
    return trasladar(trasladar(norTxt[::-1], 0, bac+bac), transN)

'''
3 Descifrado de un texto

Entrada, cifTxt -   string, texto cifrado por el mismo algoritmo
Entrada, transN -   int, posiciones salteadas del abecedario en el cifrado original
Salida -            string, texto original al cifrado (descifrado)
Descripcion:        Secuencia para descifrado: Transforma caracteres trasladando el abecedario (3.1), 
                    Permutar caracteres (3.2), Invertir orden del texto (3.3).
'''
def descifrar(cifTxt, transN = 3):
    # 3.3 Invertir orden del texto (3.2. Permutar caracteres (3.1. Transforma caracteres))
    return trasladar(trasladar(cifTxt, -transN), 0, bac+bac)[::-1]

'''
Casos de Prueba
'''

# Algoritmo Cifrado (Pasos: 1 Invertir, 2 Permutar, 3 Trasladar)
print("ABCDEFGH"[::-1]) # 1 Invertir => HGFEDCBA
print(trasladar("ABCDEFGH", 0, bac.upper(), ABC)) # 2 Permutar => BADCFEHG
print(trasladar("ABCDEFGH", 3, ABC, ABC)) # 3 Trasladar => DEFGHIJK

# Algoritmo completo cifrado y descifrado
print(descifrar("JKHIFGDE".lower())) # abcdefgh
print(cifrar("abcdefgh")) # JKHIFGDE (en minusculas)

# Normalizacion
print(normalizar("AbAbsBA.., áááéíó . ,")) # ababsbaaaaeio

# Algoritmo completo cifrado y descifrado (ultimos caracteres del abc)
print(cifrar(normalizar("fwewzy"))) # cbaiah
print(descifrar(cifrar(normalizar("fwewzy")))) # fwewzy

# # Ejemplo en Letra (inconcluso)
# cifradoLetra = "msejiwihwxeievstixgvwiniweirpqvivemjwghihsymikrwgsedilenrwqixiiwivwzhiyimtwwrimsegmxmgipj"
# print(descifrar(cifradoLetra))
#
# for i in range(0, 10):
#     print(i, ' ',descifrar(cifradoLetra, i))
