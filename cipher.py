from abc import ABC, abstractmethod

class Cipher(ABC):
    """
    Abstract base class representing a generic cipher.

    This class defines the structure and interface for various types of ciphers.
    """

    _alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Class-level variable defining the alphabet

    def __init__(self):
        """
        Initialize the Cipher object.

        Parameters:
        None

        Returns:
        None
        """
        pass

    @property
    def alphabet(self):
        """
        Property method to get the alphabet used in the cipher.

        Returns:
        str: The alphabet used in the cipher.
        """
        return self._alphabet

    def encrypt_message(self, message):
        """
        Encrypts a given message using the cipher.

        Parameters:
        message (str): The message to be encrypted.

        Returns:
        str: The encrypted message.
        """
        encrypted_message = ""
        for char in message.upper():
            if char.isalpha():
                encrypted_message += self._encrypt_letter(char)
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt_message(self, message):
        """
        Decrypts a given message using the cipher.

        Parameters:
        message (str): The message to be decrypted.

        Returns:
        str: The decrypted message.
        """
        decrypted_message = ""
        for char in message.upper():
            if char.isalpha():
                decrypted_message += self._decrypt_letter(char)
            else:
                decrypted_message += char
        return decrypted_message

    @abstractmethod
    def _encrypt_letter(self, letter):
        """
        Abstract method to encrypt a single letter using the cipher.

        Parameters:
        letter (str): The letter to be encrypted.

        Returns:
        str: The encrypted letter.
        """
        pass

    @abstractmethod
    def _decrypt_letter(self, letter):
        """
        Abstract method to decrypt a single letter using the cipher.

        Parameters:
        letter (str): The letter to be decrypted.

        Returns:
        str: The decrypted letter.
        """
        pass
