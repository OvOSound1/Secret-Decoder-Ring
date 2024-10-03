from cipher import Cipher

class AtbashCipher(Cipher):
    """
    Class representing an Atbash cipher.

    This cipher is a specific type of substitution cipher where each letter in
    the plaintext is replaced by a letter at a fixed distance away from it in
    the reverse alphabet.

    Inherits from the Cipher class.
    """

    def __init__(self):
        """
        Initialize the AtbashCipher object.

        Parameters:
        None

        Returns:
        None
        """
        super().__init__()  # Call the constructor of the parent class

    def _encrypt_letter(self, letter):
        """
        Encrypts a single letter using the Atbash cipher.

        Parameters:
        letter (str): The letter to be encrypted.

        Returns:
        str: The encrypted letter.
        """
        index = self.alphabet.index(letter)  # Find the index of the letter in the alphabet
        encrypted_index = 25 - index  # Calculate the encrypted index using the Atbash cipher rule
        return self.alphabet[encrypted_index]  # Return the encrypted letter

    def _decrypt_letter(self, letter):
        """
        Decrypts a single letter using the Atbash cipher.

        Parameters:
        letter (str): The letter to be decrypted.

        Returns:
        str: The decrypted letter.
        """
        index = self.alphabet.index(letter)  # Find the index of the letter in the alphabet
        decrypted_index = 25 - index  # Calculate the decrypted index using the Atbash cipher rule
        return self.alphabet[decrypted_index]  # Return the decrypted letter

