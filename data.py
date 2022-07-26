import re
import pandas as pd
import wordfreq

def create_wordfile(filename):
    d = open("words_alpha.txt", "r")
    five = open(filename, "w")
    for line in d.readlines():
        if re.search(r"^.{5}\n$", line):
            five.write(line)
    d.close()
    five.close()

def calc_bits(word, dat, response):
    if len(response) < 5:
        response = response + "g"
        calc_bits()

def possibilities(word, dat, response):
    for 

create_wordfile("5words.txt")
words = open("5words.txt", "r")
guess_stats = pd.DataFrame(columns = ["word", "bits", "freq"])
guess_stats["word"] = words.readlines()
guess_stats["word"] = guess_stats["word"].str.strip()
print(guess_stats.head())
for i in guess_stats.iterrows():
    

