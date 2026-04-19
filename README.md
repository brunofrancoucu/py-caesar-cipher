# Caesar Cipher

Monoalphabetic substitution cipher.

## Algorithm

1. Normalize Text

    1. Lowercase accented characters (á, é, í, ...).
    2. Keeps only alphabet characters.

2. Cipher (Normalized text)

    1. Invert order
    2. Map swap 
    3. Shift(n) 

3. Decryption
    1. Shift(-n)
    2. Map Swap 
    3. Invert order

## Terminology

- `raw_input`: Original data provided by the user to the cipher.

- `plaintext`: Data given to encription algorithm (normalized). Information pending input to encryption algorithm.

- `ciphertext`: Result produced by the encryption algorithm.

- `recovered_plaintext`: Result of decryption, matches plaintext.


## Architecture (Isolated functions)

- **Idiomatic Code**: Writing code that follows the "natural" style of the language. In Python and modern TypeScript, standalone functions are often considered more idiomatic than classes that don't hold state.

>When comparing Utility class vs standalone functions

- **Tree-shaking (TS/JS)**: Classes are much harder to tree-shake. If a library has 100 functions but you only import `ecnrypt`, modern bundlers will "shake off" the other 99.

- **Module-Level Namespacing**: In Python, the file name is the namespace. Example a class inside a file makes it cipher.Cipher.encrypt(), which is redundant ("**Stuttering**").

## TODO

- Skip user normalization step. Encryption should validate, not normalize. `decrypt(encrypt(x)) == x` byte for byte, or "Hola, mundo!".encode("utf-8")

```python
if not is_valid(plaintext):
    raise ValueError("Invalid input format")
```

<!-- Primer trabajo Grupal Programación 1 - Primer semestre 2025 -->
