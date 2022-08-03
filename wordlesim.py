import wordfreq
import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import pickle

def simulate(wordlist, dat):
    stats = []
    for word in wordlist:
        stats.append(data.simwordle(word.strip(), dat))
    return stats

#data.create_files("5words")

#words = open("5words.txt", "r")
#pic = open("5words.pickle", "rb")
#df = pd.DataFrame(pickle.load(pic))
#print(df.head(), len(df))
#stuff = simulate(words.readlines(), df)
stuff = open("max5wordle.pickle", "rb")
stats = pickle.load(stuff)
xs = [1, 2, 3, 4, 5, 6, 7]
ys = []
for i in range(1, 8):
    ys.append(stats.count(i))
print(ys)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(xs, ys)
plt.plot(xs, ys)
plt.show()