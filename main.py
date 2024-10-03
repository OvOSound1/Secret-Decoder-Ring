from atbash import AtbashCipher
from caesar import CaesarCipher
from check_input import get_int_range

def main():
    """Main function to execute the secret decoder ring program."""
    # Displaying menu options for encryption or decryption
    print("Secret Decoder Ring:")
    print("1. Encrypt")
    print("2. Decrypt")

    # Getting user's choice and ensuring it's within the specified range
    choice = get_int_range("Enter choice: ", 1, 2)

    if choice == 1:  # If user chooses encryption
        print("1. Atbash")
        print("2. Caesar")
        encryption_choice = get_int_range("Enter encryption type: ", 1, 2)

        if encryption_choice == 2:  # If user chooses Caesar encryption
            message = input("Enter message: ")  # Getting message from user
            shift = get_int_range("Enter shift value (0-25): ", 0, 25)  # Getting shift value from user
            cipher = CaesarCipher(shift)  # Creating CaesarCipher object with given shift
        else:  # If user chooses Atbash encryption
            message = input("Enter message: ")  # Getting message from user
            cipher = AtbashCipher()  # Creating AtbashCipher object

        encrypted_message = cipher.encrypt_message(message)  # Encrypting the message

        # Writing encrypted message to a file
        with open("message.txt", "w") as file:
            file.write(encrypted_message)

        print("Encrypted message saved to 'message.txt'.")
    elif choice == 2:  # If user chooses decryption
        print("1. Atbash")
        print("2. Caesar")
        decryption_choice = get_int_range("Enter decryption type: ", 1, 2)

        if decryption_choice == 2:  # If user chooses Caesar decryption
            shift = get_int_range("Enter shift value (0-25): ", 0, 25)  # Getting shift value from user
            cipher = CaesarCipher(shift)  # Creating CaesarCipher object with given shift
        else:  # If user chooses Atbash decryption
            cipher = AtbashCipher()  # Creating AtbashCipher object

        print("Reading encrypted message from 'message.txt'.")
        # Reading encrypted message from file
        with open("message.txt", "r") as file:
            encrypted_message = file.read()

        decrypted_message = cipher.decrypt_message(encrypted_message)  # Decrypting the message
        print("Decrypted message:", decrypted_message)  # Displaying decrypted message

if __name__ == "__main__":
    main()
