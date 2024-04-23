# Advanced Encryption Standard (AES) algorithm

import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt_file(file_path, password):
    # Generate a key from the password using PBKDF2HMAC
    salt = os.urandom(16)
    
    # Password-Based Key Derivation Function 2 with HMAC (convert from user given password to a key)
    # HMAC stands for Hash-based Message Authentication Code
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,      # 32 bytes = 256 bits
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Open the input file (read plain text)
    with open(file_path, 'rb') as infile:
        plaintext = infile.read()

    # Pad the plaintext to be a multiple of AES block size
    # Use PKCS7, a method used to pad input data to a specific block size before encryption
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Generate a random initialization vector
    # IV is used to ensure that each ciphertext produced with the same key is unique.
    iv = os.urandom(16)

    # Create AES cipher object
    # It creates an AES cipher object with the derived key and IV, then encrypts the padded plaintext using AES in CBC mode.
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    # Write the salt, IV, and ciphertext to the original file
    with open(file_path, 'wb') as outfile:
        outfile.write(salt)
        outfile.write(iv)
        outfile.write(ciphertext)

    print("File encrypted successfully.")

def decrypt_file(file_path, password):
    # Read the salt, IV, and ciphertext from the encrypted file
    with open(file_path, 'rb') as infile:
        salt = infile.read(16)
        iv = infile.read(16)
        ciphertext = infile.read()

    # Generate the key from the password and salt using PBKDF2HMAC
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Create AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    # Write the decrypted plaintext to the original file
    with open(file_path, 'wb') as outfile:
        outfile.write(plaintext)

    print("File decrypted successfully.")

def main():
    file_path = input("Enter the path to the file: ")
    if not os.path.exists(file_path):
        print("File not found.")
        return

    mode = input("Enter 'e' for encryption or 'd' for decryption: ")
    password = input("Enter the password: ")

    if mode == 'e':
        encrypt_file(file_path, password)
    elif mode == 'd':
        decrypt_file(file_path, password)
    else:
        print("Invalid mode. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
