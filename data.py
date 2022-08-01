import re
import pandas as pd
import time
import wordfreq
import pickle
import math

counter = 0

def create_files(filename):
    d = open("words_alpha.txt", "r")
    five = open(filename + ".txt", "w")
    for line in d.readlines():
        if re.search(r"^.{5}\n$", line):
            five.write(line)
    d.close()
    five.close()
    words = open(filename + ".txt", "r")
    guess_stats = pd.DataFrame(columns = ["word", "bits"])
    guess_stats["word"] = words.readlines()
    guess_stats["word"] = guess_stats["word"].str.strip()
    buckets = create_dictionary(dict(), "")
    guess_stats["bits"] = guess_stats["word"].map(lambda x: calc_bits(x, guess_stats["word"], buckets))
    with open(filename + ".pickle", "wb") as pi:
        pickle.dump(guess_stats, pi)

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

def check_word(to_check, regex, yellow):
    if re.match(regex, to_check):
        for k in yellow.keys():
            if yellow[k] < 0 and to_check.count(k) != -1*yellow[k]:
                return False
            elif yellow[k] > 0 and to_check.count(k) < yellow[k]:
                return False
        return True
    return False

def possibilities(word, dat, pat):
    outcome = construct_regex(word, pat)
    dat["drop"] = dat["word"].map(lambda x: check_word(x, outcome[0], outcome[1]))
    return dat[dat["drop"] == False]

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

def construct_regex(word, response):
    d = dict()
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
    return r, d

def simwordle(answer, dat):
    guesses = []
    d = create_dictionary(dict(), "")
    guesses.append(dat.loc[dat["bits"]==dat["bits"].max(), "word"])
    guesses["drop"] = False
    while len(guesses) < 7 and guesses[len(guesses)-1]["word"] != answer:
        dat = possibilities(guesses[len(guesses)-1]), dat, construct_word_code(guesses[len(guesses)-1]["word"], answer)
        dat["bits"] = dat["word"].map(lambda x: calc_bits(x, dat["word"], d))
        guesses.append(dat.loc[dat["bits"]==dat["bits"].max()])
    return len(guesses)
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
