from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os


# Generate a key for decryption
def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key



# Decrypt the file
def decrypt_file(encrypted_file_path, key, salt_file_path):
    with open(salt_file_path, "rb") as salt_file:
        salt = salt_file.read()

    with open(encrypted_file_path, "rb") as enc_file:
        encrypted_data_with_iv = enc_file.read()

    iv = encrypted_data_with_iv[:16]  # Extract IV from the start
    encrypted_data = encrypted_data_with_iv[16:]  # The rest is the encrypted data

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()



    # Create the decrypted file path in the same folder as the salt file
    decrypted_file_path = os.path.join(os.path.dirname(salt_file_path), os.path.basename(encrypted_file_path).replace(".enc", ""))

    with open(decrypted_file_path, "wb") as dec_file:
        dec_file.write(decrypted_data)

    return decrypted_file_path

if __name__ == "__main__":
    encrypted_file_path = input("Enter the path to the encrypted file (e.g., /path/to/file.txt.enc): ")
    salt_file_path = input("Enter the path to the salt file (e.g., /path/to/salt.bin): ")

    password = input("Enter the password to derive the decryption key: ")

    # Read the salt and generate the decryption key
    with open(salt_file_path, "rb") as salt_file:
        salt = salt_file.read()

    key = generate_key(password, salt)



    # Decrypt the file
    decrypted_file_path = decrypt_file(encrypted_file_path, key, salt_file_path)
    print(f"File decrypted and saved as {decrypted_file_path}")
