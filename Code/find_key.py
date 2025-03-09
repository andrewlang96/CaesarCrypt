import pandas as pd
import string

class KeyFinder:
    def __init__(self, model, encrypted_message):
        self.par_freq_df = pd.read_csv(model)
        key_pro = {k:0 for k in range(0, 26)} #Keys 0-25 and the probabilety that they are the correct key
        self.encrypted_message = encrypted_message
        self.alphanum = {k:v for (k, v) in zip(string.ascii_lowercase, range(1, 27))} #Map letters to numbers
        self.pair_space = {} #Spacing : (pair, freq)


    def make_pairspace(self):
        pairs = [pair for pair in self.par_freq_df["Pairs"]]
        freqs = [freq for freq in self.par_freq_df["Freq"]]
        for i, pair in enumerate(pairs):
            space = (self.alphanum[pair[1]] - self.alphanum[pair[0]]) % 26
            if space not in self.pair_space:
                self.pair_space[space] = [[pair[0], freqs[i]]]
            else:
                self.pair_space[space].append([pair[0], freqs[i]])






def main():
    kf1 = KeyFinder("model.csv", "message")
    kf1.make_pairspace()
    print(kf1.pair_space)


if __name__ == "__main__":
    main()
