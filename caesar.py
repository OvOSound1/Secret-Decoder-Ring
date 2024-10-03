from cipher import Cipher

class CaesarCipher(Cipher):
    """
    Class representing a Caesar cipher.

    This cipher is a type of substitution cipher where each letter in the plaintext
    is shifted a certain number of places down or up the alphabet.

    Inherits from the Cipher class.
    """

    def __init__(self, shift):
        """
        Initialize the CaesarCipher object with a specified shift.

        Parameters:
        shift (int): The number of positions to shift the alphabet for encryption/decryption.

        Raises:
        ValueError: If the shift value is not between 0 and 25.
        """
        super().__init__()  # Call the constructor of the parent class
        if 0 <= shift <= 25:  # Checking if the shift value is within the valid range
            self.shift = shift  # Assigning the shift value
        else:
            raise ValueError("Shift value must be between 0 and 25")

    def _encrypt_letter(self, letter):
        """
        Encrypts a single letter using the Caesar cipher.

        Parameters:
        letter (str): The letter to be encrypted.

        Returns:
        str: The encrypted letter.
        """
        index = self.alphabet.index(letter)  # Find the index of the letter in the alphabet
        encrypted_index = (index + self.shift) % 26  # Calculate the encrypted index using the Caesar cipher rule
        return self.alphabet[encrypted_index]  # Return the encrypted letter

    def _decrypt_letter(self, letter):
        """
        Decrypts a single letter using the Caesar cipher.

        Parameters:
        letter (str): The letter to be decrypted.

        Returns:
        str: The decrypted letter.
        """
        index = self.alphabet.index(letter)  # Find the index of the letter in the alphabet
        decrypted_index = (index - self.shift) % 26  # Calculate the decrypted index using the Caesar cipher rule
        return self.alphabet[decrypted_index]  # Return the decrypted letter
