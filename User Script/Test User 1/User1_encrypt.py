from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64
import subprocess  # To run the curl command



# Generate a key for encryption
def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,   #Aes256-  256bits
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key



# Encrypt the file
def encrypt_file(file_name, key, iv, salt):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()
    encrypted_data_with_iv = iv + encrypted_data

    base_name = os.path.splitext(file_name)[0]
    folder_name = f"Process/{os.path.basename(base_name)}"
    os.makedirs(folder_name, exist_ok=True)

    encrypted_file_path = os.path.join(folder_name, os.path.basename(file_name) + ".enc")
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data_with_iv)



    # Save the salt to the same folder
    salt_file_path = os.path.join(folder_name, "salt.bin")
    with open(salt_file_path, "wb") as salt_file:
        salt_file.write(salt)

    return encrypted_file_path




# Upload the encrypted file to Nextcloud using curl
def upload_to_nextcloud(encrypted_file_path):
    # Modify this with your Nextcloud credentials and folder
    nextcloud_user = "Tester1:@Secret5858"  # Replace with your username:password
    nextcloud_folder_url = "https://aimancloud.online/remote.php/webdav/My%20Test%20Folder/"  # Replace with your Nextcloud folder URL

    # Construct the curl command
    curl_command = [
        "curl", "-u", nextcloud_user,
        "-T", encrypted_file_path,
        nextcloud_folder_url
    ]

    try:
        result = subprocess.run(curl_command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"File successfully uploaded to Nextcloud: {nextcloud_folder_url}")
        else:
            print(f"Error uploading file: {result.stderr}")
    except Exception as e:
        print(f"An error occurred during the upload: {e}")

if __name__ == "__main__":
    password = input("Enter a password to derive the encryption key: ")
    salt = os.urandom(16)  # Generate a random salt
    iv = os.urandom(16)  # Generate a random IV
    key = generate_key(password, salt)

    file_name = input("Enter the file name to encrypt: ")
    encrypted_file_path = encrypt_file(file_name, key, iv, salt)

    print(f"File {file_name} encrypted and saved as {encrypted_file_path}")

    # Upload the encrypted file automatically to Nextcloud
    upload_to_nextcloud(encrypted_file_path)
