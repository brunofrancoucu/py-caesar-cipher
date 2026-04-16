from config import abc, abcAc, ABC, ABCAc, bac

def normalize(raw_input):
    """Cleans text: lowercase, no accents, no symbols.

    Args:
        raw_input (str): The raw string to be normalized.

    Returns:
        str: A cleaned string (lowercase, no accents, letters only).
    """

    # 1.1 All chars to abc from abcAc+abc+ABC+ABCAc
    return _transform(raw_input, 0, abc+abc+abc+abc, abcAc+abc+ABC+ABCAc)

def encrypt(nomral_plaintext, shift_n = 3):
    """Steps: Reverse -> Permute -> Shift.

    Args:
        normal_plaintext (str): A pre-normalized string.
        shift_n (int): Number of positions to shift in the final step.

    Returns:
        str: The final encrypted ciphertext.
    """

    # 2.3. Shift(n) (2.2 Map swap (2.1 Invert order))
    return _transform(_transform(nomral_plaintext[::-1], 0, bac+bac), shift_n)

def decrypt(ciphertext, shift_n = 3):
    """Steps: Un-shift -> Un-permute -> Reverse.

    Args:
        ciphertext (str): The string encrypted by this algorithm.
        shift_n (int): The original shift value used during encryption.

    Returns:
        str: The decrypted original plaintext.
    """

    # 3.3 Invert order (3.2. Map Swap (3.1. Shift(-n)))
    return _transform(_transform(ciphertext, -shift_n), 0, bac+bac)[::-1]

# Helpers

def _transform(inStr, n = 3, outMap = abc+abc, inMap = abc+abc):
    """Internal helper for mapping and shifting.

    Args:
        str (str): String containing characters to be translated.
        n (int): Number of positions to skip/shift within `outMap`.
        outMap (str): The target mapping/output alphabet.
        inMap (str): The source mapping/input alphabet used to find positions.

    Returns:
        str: The processed string with characters mapped and shifted.
    """

    # Map `inStr` characters from `inMap` to a `n` shifted `outMap` (when .find() !== -1)
    return "".join(outMap[inMap.find(char) + n] for char in inStr if char in inMap)
