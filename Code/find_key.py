import pandas as pd
import string

class KeyFinder:
    def __init__(self, model, encrypted_message):
        self.par_freq_df = pd.read_csv(model, nrows=30)
        self.key_pro = {k:0 for k in range(0, 26)} #Keys 0-25 and the probabilety that they are the correct key
        self.encrypted_message = encrypted_message
        self.alphanum = {k:v for (k, v) in zip(string.ascii_lowercase, range(1, 27))} #Map letters to numbers
        self.pair_space = {} #Spacing : (pair, freq)
        self.alpha = string.ascii_lowercase


    def make_pairspace(self): #Restructure model to facilitate decoding.
        pairs = [pair for pair in self.par_freq_df["Pairs"]]
        freqs = [freq for freq in self.par_freq_df["Freq"]]
        for i, pair in enumerate(pairs):
            space = (self.alphanum[pair[1]] - self.alphanum[pair[0]]) % 26 #Distance between the two letters in pair
            if space not in self.pair_space:
                self.pair_space[space] = [(pair[0], freqs[i])]
            else:
                self.pair_space[space].append((pair[0], freqs[i]))


    def get_probs(self):
        for i, char in enumerate(self.encrypted_message):
            try: #This block should throw and index erro on the last element of the string.
                if char not in self.alpha or self.encrypted_message[i + 1] not in self.alpha:
                    continue
            except IndexError:
                break
            space = (self.alphanum[self.encrypted_message[i + 1]] - self.alphanum[char]) % 26
            if space in self.pair_space:
                for j in self.pair_space[space]:
                        self.key_pro[((self.alphanum[j[0]]) - self.alphanum[char]) % 26] += j[1]
        freq_sum = 0
        for i in self.key_pro: #Add up frequences
            freq_sum += self.key_pro[i]
        self.key_pro = {k:(v / freq_sum) for (k, v) in self.key_pro.items() if (v != 0 and v > 0.01)} #Normalize probs and remove prob < 0.01


def main():
    kf1 = KeyFinder("model.csv", "hvwg kwzz oqhiozzm ps sbqfmdhsr bck")
    kf1.make_pairspace()
    kf1.get_probs()
    # print(kf1.pair_space)
    print(kf1.key_pro)


if __name__ == "__main__":
    main()
