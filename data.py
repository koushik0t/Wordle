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

def create_dictionary(d, response):
    if len(response) < 5:
        temp = response + "!"
        d = create_dictionary(d, temp)
        temp = response + "?"
        d = create_dictionary(d, temp)
        temp = response + "."
        d = create_dictionary(d, temp)
        return d
    else:
        d[response] = 0
        return d

def calc_bits(word, dat, d):
    count = 0
    sum = 0
    for k in d.keys():
        d[k] = possibilities(word, dat, k)
        if d[k] > 0:
            sum += d[k]
            count += 1
    return sum/count


def possibilities(word, dat, pat):
    outcome = construct_regex(word, pat)
    count = 0
    for i in dat:
        if re.match(outcome[0], word) and outcome[1] in word:
            count += 1
    return count

def construct_regex(word, response):
    r = ""
    gray = ""
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
    ret = ""
    for i in range(0, len(response)):
        if 
        
    r = r.replace(" ", gray)
    return r + "," + yellow

create_wordfile("5words.txt")
words = open("5words.txt", "r")
guess_stats = pd.DataFrame(columns = ["word", "bits", "freq"])
guess_stats["word"] = words.readlines()
guess_stats["word"] = guess_stats["word"].str.strip()
print(guess_stats.head())
buckets = create_dictionary(dict(), "")
print(len(buckets.keys()))