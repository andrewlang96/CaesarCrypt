import string

class Crypt:
    def __init__(self, message, key, decrypt=False):
        """
        Encrypt of decrypte english text with a caesar cypher.
        vars:
            message (str): The string that is to be encrypted or decrypted
            key (int): An integer 1-25 that is used to encrypt or decrypt the string
            decrypt (bool): If decrypt, the class will be set to decrypt the message. otherwise it will encrypt it
        """
        self.message = message.lower()
        if decrypt: #Crypt is set to decrypt instead of encrypt.
            self.key = (26 - key) % 26
        else:
            self.key = key % 26 #Ensure that key is a value 0-25
        alpha = list(string.ascii_lowercase)
        num = list(range(1, 27))
        self.alphanum = {k:v for (k, v) in zip(alpha, num)} #Map letters to numbers
        self.numalpha = {k:v for (k, v) in zip(list(range(1, 26)), alpha)} #Map numbers to letters
        self.numalpha[0] = "z"

    def en_decrypt(self):
        """
        Manages the encrytion/decryption of the message
        return: The encrypted/decrypted message
        """
        self.num_message = [self.alphanum[i] if i in self.alphanum else i for i in self.message] #Map message to associated numbers
        self.encrypted_num_message = [i if not isinstance(i, int) else ((i + self.key) % 26) for i in self.num_message] #Encrypt umbers with key
        self.encrypted_message = "".join([self.numalpha[i] if i in self.numalpha else i for i in self.encrypted_num_message]) #Map encrypted numbers back to letters
        return self.encrypted_message

def main():
    c1 = Crypt("This will actually be encrypted now", 12, decrypt=True)
    print(c1.en_decrypt())


if __name__ == "__main__":
    main()