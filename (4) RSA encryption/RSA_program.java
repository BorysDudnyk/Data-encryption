import java.security.*;
import javax.crypto.*;

public class Main {

    public static void main(String[] args) throws Exception {
        // Генерация ключей RSA
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // Размер ключа 2048 бит
        KeyPair keyPair = keyPairGen.generateKeyPair();

        // Получение открытого и закрытого ключей
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // Создание объекта для шифрования и дешифрования
        Cipher cipher = Cipher.getInstance("RSA");

        // Оригинальное сообщение
        String originalMessage = "Hello, World!";
        System.out.println("Original Message: " + originalMessage);

        // Шифрование сообщения с использованием открытого ключа
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] encryptedBytes = cipher.doFinal(originalMessage.getBytes());
        System.out.println("Encrypted Message: " + new String(encryptedBytes));

        // Дешифрование сообщения с использованием закрытого ключа
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
        String decryptedMessage = new String(decryptedBytes);
        System.out.println("Decrypted Message: " + decryptedMessage);
    }
}