(1) RSA algorithm

openssl genpkey -algorithm RSA -out private_key.pem
openssl rsa -pubout -in private_key.pem -out public_key.pem
openssl pkeyutl -encrypt -in lab9.txt -out encrypted.txt -inkey public_key.pem -pubin
openssl pkeyutl -decrypt -in encrypted.txt -out decrypted.txt -inkey private_key.pem

(2) AES-256 algorithm

openssl rand -out keyfile.key 32
openssl enc -aes-256-cbc -in text.txt -out encrypted.txt -pass file:keyfile.key
openssl enc -d -aes-256-cbc -in encrypted.txt -out decrypted.txt -pass file:keyfile.key

(3) SHA-256

openssl dgst -sha256 -binary -out hashed.txt text.txt
openssl dgst -sha256 -binary -out hashed_new.txt text.txt
