import pandas as pd
import string

class KeyFinder:
    def __init__(self, model, encrypted_message):
        """
        Determins that the probabiley that a given key was used to encrypt a given
        text based on a language model.
        Args:
            model ("file.csv"): A csv file produced by make_model.py that contains letter pairs and thier reletive frequency in written english.
            encrypted_message (str): A string that has been encrypted using a caesar cypher.
        """
        self.par_freq_df = pd.read_csv(model, nrows=40)
        self.key_pro = {k:0 for k in range(0, 26)} #Keys 0-25 and the probabilety that they are the correct key
        self.encrypted_message = encrypted_message
        self.alphanum = {k:v for (k, v) in zip(string.ascii_lowercase, range(1, 27))} #Map letters to numbers
        self.pair_space = {} #Spacing : (pair, freq)
        self.alpha = string.ascii_lowercase


    def make_pairspace(self):
        """
        Restructures the language model to better facilitate decoding.
        """
        pairs = [pair for pair in self.par_freq_df["Pairs"]]
        freqs = [freq for freq in self.par_freq_df["Freq"]]
        for i, pair in enumerate(pairs):
            space = (self.alphanum[pair[1]] - self.alphanum[pair[0]]) % 26 #Distance between the two letters in pair
            if space not in self.pair_space:
                self.pair_space[space] = [(pair[0], freqs[i])]
            else:
                self.pair_space[space].append((pair[0], freqs[i]))


    def get_probs(self):
        """
        Determins the probabilety that a given key was used to encrypt and encrypted message
        """
        for i, char in enumerate(self.encrypted_message):
            try: #This block should throw and index error on the last element of the string.
                if char not in self.alpha or self.encrypted_message[i + 1] not in self.alpha:
                    continue
            except IndexError:
                break
            space = (self.alphanum[self.encrypted_message[i + 1]] - self.alphanum[char]) % 26
            if space in self.pair_space:
                for j in self.pair_space[space]:
                    self.key_pro[((self.alphanum[char] - self.alphanum[j[0]])) % 26] += j[1]
        freq_sum = 0
        for i in self.key_pro: #Add up frequences
            freq_sum += self.key_pro[i]
        self.key_pro = dict(sorted(self.key_pro.items(), key=lambda i: i[1])) #Order key_pro by prob
        self.key_pro = {k:(v / freq_sum) for (k, v) in self.key_pro.items()} #Normalize probs
        self.key_pro = dict(list(self.key_pro.items())[-6:]) #Remove all but last 5 probs



def main():
    kf1 = KeyFinder("model.csv", "hvwg kwzz oqhiozzm ps sbqfmdhsr bck")
    kf1.make_pairspace()
    kf1.get_probs()
    # print(kf1.pair_space)
    print(kf1.key_pro)


if __name__ == "__main__":
    main()
