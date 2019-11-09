# AES and text steganography implementation in Python 3

Run the run.exe file to encrypt or decrypt information to/from any docx file using a key.

In this project, files and information are hidden in text documents using AES cryptography followed by Text-Steganography.

Encryption:
1.	User enters key and secret data and provides directory of cover file
2.	Key is converted to AES block size bytes with the help of padding followed by hashing
3.	AES encryption selects random iv(in the form of bytes)
4.	Secret data is encrypted by using AES encryption library by using iv,key to produce Ciypher Bytes
5.	Cipher Bytes are then added with iv and typecasted to a string after base-64 encoding
6.	String is then passed to text-steganography encrypt function where it is converted to bits and hidden inside words with the help of styling taking 2 bits at a time.

Decryption:
1.	User is prompted to enter the secret key and directory of file to be decrypted.
2.	Pairs of bits are decrypted from each word with the help of reverse styling
3.	The output string is converted into bytes with the help of Base-64 decoding
4.	From these bytes the first AES_block size bytes are iv and the rest is cipher bytes
5.	Cipher bytes are decrypted by using the user input key and iv into the required decrypted secret message.

(Decryption process traces the encryption process in reverse order )

Styling here implies the way a specific word is written ie.it's font and size, to indicate which pair of bits it represents
