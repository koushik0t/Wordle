import wordfreq
import data
import pandas as pd
import pickle

#create_files("5words")
words = open("5words.txt", "r")
pic = open("5words.pickle", "rb")
df = pd.DataFrame(pickle.load(pic))
print(df.head())

val = data.simwordle("chalk", df)