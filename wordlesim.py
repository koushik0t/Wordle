import wordfreq
import data
import pandas as pd
import matplotlib.pyplot as plt
import pickle

def simulate(wordlist, dat):
    stats = []
    for word in wordlist:
        stats.append(data.simwordle(word.strip(), dat))
    return stats

#data.create_files("5words")

words = open("5words.txt", "r")
pic = open("5words.pickle", "rb")
df = pd.DataFrame(pickle.load(pic))
print(df.head(), len(df))
stuff = simulate(words.readlines(), df)
stats = open("max5wordle.pickle", "wb")
pickle.dump(stuff, stats)
print(stuff)