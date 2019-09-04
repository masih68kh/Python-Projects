import json
import numpy as np
import pandas as pd

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


def translate(word, data):
    meanings = data[word]
    print("the word has %d meanings" % len(meanings))
    for idx , itm in enumerate(meanings):
        print("Meaning %d: " % (idx+1),itm)


with open("data.json", 'r') as jsonFile:
    data = json.load(jsonFile)
    
word = input("Input word: ").lower()
if word in data:
    translate(word, data)
else:
    similarities = []
    for wrd in data.keys():
        similarities.append( levenshtein(wrd, word) )

    dict_simil = {'word': list(data.keys()),'similarity':similarities}

    similarities_pd = pd.DataFrame(data=dict_simil)
    similarities_pd = similarities_pd.sort_values(by='similarity').head(10)

    count = 0
    for sugges in similarities_pd['word'].values:
        massage = "Do you mean {}? Press Y or N: ".format(sugges)
        answer = input(massage).lower()
        if answer == 'y':
            translate(sugges, data)
            break
    if answer != 'y':
        print("the is no meaning for '{}'".format(word))



