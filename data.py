import re

def create_wordfile(filename):
    d = open("words_alpha.txt", "r")
    five = open(filename, "w")
    for line in d.readlines():
        if re.search(r"^.{5}\n$", line):
            five.write(line)
    d.close()
    five.close()

def 

