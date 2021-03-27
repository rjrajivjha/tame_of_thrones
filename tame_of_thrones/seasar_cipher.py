import string

ENGLISH_ALPHABETS = string.ascii_lowercase


class SeasarCipher:

    @staticmethod
    def rotate_left(alphabet: str, distance: int) -> str:
        alphabet_position = ENGLISH_ALPHABETS.find(alphabet)
        rotated_position = (alphabet_position - distance) % 26
        return ENGLISH_ALPHABETS[rotated_position]

    def decrypt(self, cipher_text: str, cipher_length: int) -> str:
        decrypted_message = ""
        for alphabet in cipher_text:
            if alphabet in ENGLISH_ALPHABETS:
                decrypted_message += self.rotate_left(alphabet, cipher_length)
            else:
                decrypted_message += alphabet
        return decrypted_message
