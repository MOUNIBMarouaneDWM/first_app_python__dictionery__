import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate (word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())):
        # cutoff=0.9 (nissbat taxaaboh)
        yn = input("do you mean %s  ,(y/n) : " % get_close_matches(word,data.keys(),)[0])
        if yn.lower() =="y" or yn.lower() =="yes" :
            return data[get_close_matches(word,data.keys(),)[0]]
        else:
            return "we dont know what you mean please check again"

    else:
        return "the word does not exist. Please check it."

word_in = input("inter word: ")
print(translate(word_in))