from colorama import Fore, Back, Style
import os
import platform
import encrypt_decrypt
import find_key

class CryptInterface:
    def __init__(self, model):
        """
        A command line interface that alows user to encrypt and decrypt messages and shows info about decryption keys
        Args:
            model ("file.csv"): A csv file produced by make_model.py
        """
        self.model = model


    def clear(self):
        """
        Clear terminal window.
        """
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")


    def spacing(self, spacing):
        return  "".join([" " for i in range(spacing)])


    def header(self, tytle, spacing, frameL=">>>", frameR="<<<", color=Fore.GREEN):
        """
        Clears terminal and prints header
        Args:
            tytle (str): Header text
            spacing (int): Number of spaces from left side of screen
            frameL (str): Symbols to frame the left side of the tytle
            frameR (str): Symbols to frame the right side of the tytle
            color (Fore.COLOR): Color of frame
        """
        self.clear()
        spacing = self.spacing(spacing)
        print("\n", spacing, color, frameL, Fore.WHITE, tytle, color, frameR, "\n", Fore.WHITE)


    def key_graph(self):
        pass


    def main_loop(self):
        print(Fore.WHITE) #Set defalt text colore to white.
        while True:
            self.header("Caesar Cypher", 12)
            message = input(" Enter the message that you would like to encrypt: ").lower()
            self.header("Caesar Cypher", 12)
            while True:
                try:
                    key = int(input(" Enter the key encryption number (1-25): "))
                    break
                except ValueError:
                    print(Fore.RED, "!Key value must be an integer!", Fore.WHITE)
            crypt = encrypt_decrypt.Crypt(message, key)





def main():
    ci = CryptInterface("model.csv")
    ci.main_loop()

if __name__ == "__main__":
    main()


