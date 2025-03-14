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


    def spacing(self, spacing, char=" "):
        return  "".join([char for i in range(spacing)])



    def header(self, tytle, spacing, frameL=">>>", frameR="<<<", color=Fore.GREEN):
        """
        Clear terminal and print header
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


    def key_graph(self, encrypted_message, key_pro):
        selected = 0
        while True:
            self.header("Probable Keys", 12)
            print(Fore.GREEN, "Encrypted Message:", Fore.MAGENTA, encrypted_message)
            print("\n\n", Fore.WHITE, "\n Keys")
            bar_graph_scale = 200 #Multiplier that scales the size of the bar grapgh
            for i, key in enumerate(key_pro):
                if key > 10:
                    if i == selected:
                        print(Fore.WHITE, self.spacing(3), f"{key}:", Back.GREEN, self.spacing(round(key_pro[key] * bar_graph_scale)),
                        Style.RESET_ALL, Fore.BLUE,  f"{round(key_pro[key]*100, 2)}%\n")
                    else:
                        print(Fore.WHITE, self.spacing(3), f"{key}:", Back.BLUE, self.spacing(round(key_pro[key] * bar_graph_scale)),
                        Style.RESET_ALL, "\n")
                else:
                    if i == selected:
                        print(Fore.WHITE, self.spacing(3), f" {key}:", Back.GREEN, self.spacing(round(key_pro[key] * bar_graph_scale)),
                        Style.RESET_ALL, Fore.BLUE, f"{round(key_pro[key]*100, 2)}%\n")
                    else:
                        print(Fore.WHITE, self.spacing(3), f" {key}:", Back.BLUE, self.spacing(round(key_pro[key] * bar_graph_scale)),
                        Style.RESET_ALL, "\n")
            key_prob = list(key_pro.items())
            key = key_prob[selected][0]
            decrypt = encrypt_decrypt.Crypt(encrypted_message, key, decrypt=True)
            decrypted_message = decrypt.en_decrypt()
            print("\n", self.spacing(5), Fore.GREEN, "Decrypted Message:", Fore.CYAN, decrypted_message, Fore.WHITE, f"\n        KEY={key}")
            command = input()
            if command == "q":
                break
            else:
                selected += 1
                selected = selected % len(key_pro)


    def main_loop(self):
        print(Fore.WHITE) #Set defalt text colore to white.
        while True:
            self.header("Caesar Cypher", 12)
            message = input(" Enter the message that you would like to encrypt: ").lower()
            if message == "q":
                break
            self.header("Caesar Cypher", 12)
            while True:
                try:
                    key = int(input(" Enter the key encryption number (1-25): "))
                    break
                except ValueError:
                    print(Fore.RED, "!Key value must be an integer!", Fore.WHITE)
            crypt = encrypt_decrypt.Crypt(message, key)
            encrypted_message = crypt.en_decrypt()
            print("\n\n Encrypted message:", Fore.MAGENTA, encrypted_message,
            Fore.WHITE, "\n\n Press", Fore.GREEN, "ENTER", Fore.WHITE, "to see decryption")
            decrypt = input()
            key_finder = find_key.KeyFinder(self.model, encrypted_message)
            key_finder.make_pairspace()
            key_finder.get_probs() #Makes key_finder.key_pro which is the dict that will go to key_graph
            self.key_graph(encrypted_message, key_finder.key_pro)





def main():
    ci = CryptInterface("model.csv")
    ci.main_loop()


if __name__ == "__main__":
    main()


