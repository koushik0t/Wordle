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
        temp = response + "!"
        calc_bits(word, dat, temp)
        temp = response + "?"
        calc_bits(word, dat, temp)
        temp = response + "."
        calc_bits(word, dat, temp)
    else:
        return possibilities(word, dat, construct_regex(response))

def possibilities(word, dat, pat):
    count = 0
    for i in dat:
        if re.match(pat, word):
            count += 1
    return count

def construct_regex(word, response):
    regex = ""
    gray = "[^"
    yellow = ""
    for i in range(0, len(response)):
        if response[i] == "!":
            r = r + word[i]
        elif response[i] == "?":
            yellow = yellow + word[i]
            r = r + " "
        else:
            gray = gray + word[i]
            r = r + " "
    gray = gray + "]"
    r = r.replace(" ", gray)
    return r + "," + yellow

create_wordfile("5words.txt")
words = open("5words.txt", "r")
guess_stats = pd.DataFrame(columns = ["word", "bits", "freq"])
guess_stats["word"] = words.readlines()
guess_stats["word"] = guess_stats["word"].str.strip()
print(guess_stats.head())
print(construct_regex("hello", "!?..."))