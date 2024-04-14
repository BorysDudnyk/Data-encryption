from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def generate_aes_key():
    return os.urandom(32)

def pad_data(data):
    block_size = AES.block_size
    padding_size = block_size - len(data) % block_size
    padding = bytes([padding_size]) * padding_size
    return data + padding

def unpad_data(data):
    padding_size = data[-1]
    return data[:-padding_size]

def encrypt_file(input_file, output_file, key):
    chunk_size = 64 * 1024
    init_vector = get_random_bytes(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, init_vector)

    with open(input_file, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(init_vector)
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % AES.block_size != 0:
                    chunk = pad_data(chunk)
                outfile.write(encryptor.encrypt(chunk))
    print(f"Файл {input_file} зашифровано та збережено у файлі {output_file}")

def decrypt_file(input_file, output_file, key):
    chunk_size = 64 * 1024

    with open(input_file, 'rb') as infile:
        init_vector = infile.read(AES.block_size)
        decryptor = AES.new(key, AES.MODE_CBC, init_vector)
        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                decrypted_chunk = decryptor.decrypt(chunk)
                outfile.write(unpad_data(decrypted_chunk))
    print(f"Файл {input_file} розшифровано та збережено у файлі {output_file}")

if __name__ == "__main__":
    key = generate_aes_key()
    input_file = 'input.txt'
    encrypted_file = 'encrypted_file.enc'
    decrypted_file = 'decrypted_file.txt'

    encrypt_file(input_file, encrypted_file, key)
    decrypt_file(encrypted_file, decrypted_file, key)