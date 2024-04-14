# Алгоритми шифрування та хешування

Цей репозиторій містить приклади використання алгоритмів RSA, AES-256 та SHA-256 для шифрування, дешифрування та хешування даних за допомогою OpenSSL.

## (1) Алгоритм RSA

Алгоритм RSA є асиметричним криптографічним алгоритмом, який використовує пари ключів для шифрування та дешифрування даних.

### Команди для виконання:

1. Створення приватного та публічного ключів:
    ```bash
    openssl genpkey -algorithm RSA -out private_key.pem
    openssl rsa -pubout -in private_key.pem -out public_key.pem
    ```

2. Шифрування текстового файлу:
    ```bash
    openssl pkeyutl -encrypt -in lab9.txt -out encrypted.txt -inkey public_key.pem -pubin
    ```

3. Дешифрування текстового файлу:
    ```bash
    openssl pkeyutl -decrypt -in encrypted.txt -out decrypted.txt -inkey private_key.pem
    ```

## (2) Алгоритм AES-256

Алгоритм AES-256 є симетричним криптографічним алгоритмом, який використовує 256-бітний ключ для шифрування та дешифрування даних.

### Команди для виконання:

1. Генерація ключового файлу:
    ```bash
    openssl rand -out keyfile.key 32
    ```

2. Шифрування текстового файлу:
    ```bash
    openssl enc -aes-256-cbc -in text.txt -out encrypted.txt -pass file:keyfile.key
    ```

3. Дешифрування текстового файлу:
    ```bash
    openssl enc -d -aes-256-cbc -in encrypted.txt -out decrypted.txt -pass file:keyfile.key
    ```

## (3) SHA-256

SHA-256 є криптографічним хеш-алгоритмом, який створює 256-бітний (32-байтовий) хеш текстового файлу.

### Команди для виконання:

1. Хешування текстового файлу:
    ```bash
    openssl dgst -sha256 -binary -out hashed.txt text.txt
    ```

2. Хешування текстового файлу з іншим вихідним файлом:
    ```bash
    openssl dgst -sha256 -binary -out hashed_new.txt text.txt
    ```

## Висновок

Цей README містить базові приклади використання алгоритмів RSA, AES-256 та SHA-256 з OpenSSL. Використовуйте ці приклади для шифрування, дешифрування та хешування даних.
