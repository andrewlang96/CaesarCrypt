import pandas as pd
import string

class Model:
    def __init__(self, training_text):
        """
        Reads through an text and determins the rate of occurance of letter pairs within the text.
        Args:
            training_text ("file.txt"): The text that will be read to determin the frequency of letter pairs.
        """
        text_file = open(training_text, "r")
        self.training_text = text_file.read().lower()
        self.possible_keys = {k:0 for k in range(0, 26)}
        self.adj_pairs = {}
        self.pair_count = 0
        self.alpha = list(string.ascii_lowercase)

    def make_model(self, csv_file):
        """
        Reads the text and writes the letter pair frequencies to a csv file.
        Args:
            csv_file ("file/csv"): The csv file that the data will be written to.
        """
        for i, char in enumerate(self.training_text):
            try:
                if (char not in self.alpha) or (self.training_text[i + 1] not in self.alpha): #The current carecter or th one that fallows is not a letter.
                    continue
                elif (char  + self.training_text[i + 1]) not in self.adj_pairs: #The current pair has not been added yet
                    self.adj_pairs[char + self.training_text[i + 1]] = 1
                    self.pair_count += 1
                else:
                    self.adj_pairs[char + self.training_text[i + 1]] += 1 #The currnet pair has been added
                    self.pair_count += 1
            except IndexError: #IndexError on last char
                break
        self.adj_pairs = {k:(self.adj_pairs[k]/self.pair_count) for k in self.adj_pairs} #Convert from pair count to pari frequency
        self.adj_pairs = dict(sorted(self.adj_pairs.items(), key=lambda i: i[1], reverse=True)) #Order pairs by frequency
        lables = ["Pairs", "Freq"] #Lables for columns of DataFrame
        columns = [list(self.adj_pairs), list(self.adj_pairs.values())] #Columns of DataFrame
        self.pair_df = pd.DataFrame({k:v for (k, v) in zip(lables, columns)}) #Make DataFrame of pairs and frequencies
        self.pair_df.to_csv(csv_file, index=False) #Write DataFrame to csv file

def main():
    m1 = Model("training_text.txt")
    m1.make_model("model.csv")
    print(m1.pair_df, f"\nTotal Pairs: {m1.pair_count}\nUnique Pairs: {len(m1.adj_pairs)}")



if __name__ == "__main__":
    main()