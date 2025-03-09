
	The purpose of this program is to decrypt English text (though this method probably works on other languages) that has been encrypted using a Caeser cypher.

DecryptionCaeser Outline

-Encryption
	First each letter in the alphaben must be assigned a number 1 - 26. The user will provide the string of text that they would like to have encrypted as well as
	a key value that will be used to encrypt the text (1 - 25). The provided string will be converted into a list of its associated numeric values ("abc" --> 1,2,3) and then
	the key value will be added mod26 to each of the associated values. Finally the numbers will be mapped backed 	to letters to produce the encrypted string.
	Example:
		string = "the string"
		key = 7
		num_string = [20, 8, 5,  , 19, 20, 18, 9, 14, 7]
		encrypted_num_string = [1, 15, 12,  , 26, 1, 25, 16, 21, 14]
		encrypted_string = "aol zaypun"

-Model Building
	This model is based on tracking the average rate of occurance of pairs of adjecent letters in written English. This is done by reading through a training text
	(prefferabley a large 		text) and identifying each unique adjecent letter pair (unique_adja_pairs("the") = ["th", "he"]), and how many times it occures with respect
	to the total number of adjacent letter 		pairs (total_adja_pairs("the") = 2). The model also uses the distance between the letteres in these pairs. This distance is important
	because while the caeser cypher changes the value 	of each letter, it does not change the distance between each adjacent pair of letters.
	Example:
		*********** PAIR COUNT ***************
		training_text = "This is the training text." #The real training text is much longer
		unique_pair_count = { # pair : count
				"th" : 2, "hi" : 1,
				"is" : 2, "he" : 1,
				"tr" : 1, "ra" : 1,
				"ai" : 1, "in" : 2,
				"ni" : 1, "ng" : 1,
				"te" : 1, "ex" : 1,
				"xt" : 1
				}
		total_pair_count = 16 #Total number of adjacent letter pairs in training_text
		pair_rate = { #pair : unique_pair_count[pair]/total_pair_count
				"th" : 0.125,
				"hi" : 0.0625,
				"is" : 0.125,
				"he" : 0.0625,
				"tr" : 0.0625,
				"ra" : 0.0625,
				"ai" : 0.0625,
				"in" : 0.125,
				"ni" : 0.0625,
				"ng" : 0.0625,
				"te" : 0.0625,
				"ex" : 0.0625,
				"xt" : 0.0625
		************* PAIR DISTANCE *******************
		Pair distance are founnd by taking the diffeence of the numeric values ("abc" --> 1,2,3) of the letters
		in the pair. if the value of the first letter is less than the value of the second ("ht" --> 8,20), then the
		distance is equal to the value of the second letter minus the value of the first (dist("ht")= 20 - 8 = 12). Otherwise the distance
		is equal to the value of the second letter minus the value of the first plus 26. (dist("th") = 8 + (26 - 20) = 14)
		unique_pair_spacing = { #pair : distance
					"th" : 14,
					"hi" : 1
					"is" : 10,
					"he" : 23,
					"tr" : 24,
					"ra" : 9,
					"ai" : 8,
					"in" : 6,
					"ni" : 21,
					"ng" : 19,
					"te" : 11,
					"ex" : 19,
					"xt" : 22
					}
		The final model associates distances with a list of tuples of pairs and pair frequencies (distance : [(pair1, freq1) ... (pair_n, freq_n)])
		model = {
			1 : [("hi", 0.0625)],
			6 : [("in", 0.125)],
			8 : [("ai", 0.0625)],
			9 : [("ra", 0.0625)],
			10 : [("is", 0.125)],
			11 : [("te", 0.0625)],
			14 : [("th", 0.125)],
			19 : [("ng", 0.0625), ("ex", 0.0625)],
			21 : [("ni", 0.0625)],
			22 : [("xt", 0.0625)],
			23 : [("he", 0.0625)],
			24 : [("tr", 0.0625)]
			}
		The above dictionary is a full model based on the training text that was given at the start. Because the training text is so short
		the model is completely useless, but the prosses used to develope it is the same that one would use with a large training text. This
		dictionary would then be converted to a pandas data fram and writen to a csv file so that it could be easly read into another file.
		How this model is used to decrypt a string of encrypted text will be shown later.

-Decrypt Text
    Decrypting the encrypted text consists of using the model to pretict what the key probably is, and then using the key to produce an inverse
    key. An inverse key is a key that if use to encrypt the encrypted text would return it to its orgiginal state.
    To submit the encrypted text to the model, we first list out the adjacent letter pairs in the encryted text along with their associated
    distances (encrypted_pair = "ao" : distance = 14).
    Example:
        **************** USE MODEL TO FIND KEY ****************
        encrypted_text = "aol zypun" #This string has been encrypted using key = 7.
        encrypted_pair_spacing = { #pair : distance
            					"ao" : 14,
            					"ol" : 23
            					"zy" : 25,
            					"yp" : 17,
            					"pu" : 5,
            					"un" : 19,
            					}

