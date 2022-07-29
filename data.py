import re
import pandas as pd
import time
import wordfreq
import pickle
import math

counter = 0

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
    sum = 0.0
    for possible in dat:
        key = construct_word_code(word, possible)
        d[key] += 1
    for k in d.keys():
        if d[k] > 0:
            p = d[k]/len(dat)
            sum += -1*p*math.log(p, 2)
            d[k] = 0
    global counter
    counter += 1
    if counter % 50 == 0:
        print(word)
        print(sum)
    return sum


def possibilities(word, dat, pat):
    outcome = [1, 2]
    print("pattern is: " + outcome[0])
    count = 0
    for possible in dat:
        if re.match(outcome[0], possible):
            y = True
            for j in outcome[1].keys():
                rep = possible.count(j)
                if rep < abs(outcome[1][j]) or (outcome[1][j] < 0 and rep > outcome[1][j]*-1):
                    y = False
            if y:
                count+=1
    return count

def construct_word_code(word, target):
    r = ""
    for i in range(0, len(word)):
        if word[i] == target[i]:
            r = r + "!"
        elif word[i] in target and r.count("?") < target.count(word[i]):
            r = r + "?"
        else:
            r = r + "."
    return r
    """d = dict()
    r = ""
    if response == "":
        return r, d
    gray = ""
    for i in range(0, len(response)):
        if response[i] == ".":
            gray = gray + word[i]
    for i in range(0, len(response)):
        if response[i] == "!":
            r = r + word[i]
        elif response[i] == "?":
            r = r + "[^" + gray + word[i] + "]"
            if word[i] not in d.keys():
                d[word[i]] = 0
            if word[i] in gray:
                d[word[i]] -= 1
            else:
                d[word[i]] += 1
        else:
            r = r + "[^" + gray + "]"
    return r, d"""

create_wordfile("5words.txt")
words = open("5words.txt", "r")
guess_stats = pd.DataFrame(columns = ["word", "bits"])
guess_stats["word"] = words.readlines()
pi = open("wordle_begin.txt", "w")
pickle.dump(guess_stats, "wordle_begin.txt")
guess_stats["word"] = guess_stats["word"].str.strip()
buckets = create_dictionary(dict(), "")
guess_stats["bits"] = guess_stats["word"].map(lambda x: calc_bits(x, guess_stats["word"], buckets))
pi = open("wordle_begin.txt", "w")
pickle.dump(guess_stats, pi)
print(guess_stats.head())