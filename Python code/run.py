import AES as crypto
import text_stegano as stegno
import base64

def encryption():
    key = input("Enter the key: ")
    var = crypto.aes(key)
    plain_text = input("Enter the secret data: ")
    cypher_text = var.encrypt(plain_text)
    data_str = (str)(base64.b64encode(cypher_text))
    stegno.encrypt(data_str)
    while True:
        action = input("Do you want information regarding AES - cryptography? (y/n) ")
        if action == 'y':
            print("Cypher text: ")
            print(cypher_text)
            print("Base64 encoded format of cypher text: " + data_str[2:-1])
            break
        if action == 'n':
            break


def decryption():
    key = input("Enter the key: ")
    var = crypto.aes(key)
    data_str = stegno.decrypt()
    cypher_text = base64.b64decode(data_str[1:])
    try:
        plain_text = var.decrypt(cypher_text)
        print("Decoded text is: " + plain_text)
    except:
        print("Wrong key try again")


def main():
    while True:
        print("")
        action = input("Do you want to perform encryption(e), decryption(d) or exit: ")
        if action == 'e':
            encryption()
        elif action == 'd':
            decryption()
        elif action == 'exit':
            break
        else:
            print("Invalid input try again")


if __name__ == '__main__':
    main()
