import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def definer(word):  
    w = word.lower()
    if w in data: 
        return data[w]
    elif w.title() in data: 
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        inp =  input("Did you mean to say %s? Type in Y if Yes or N if NO: " % get_close_matches(w, data.keys())[0])
        if inp == "Y":
            return data[get_close_matches(w, data.keys())]
        elif inp == "N":
            return "Please double check your input"
        else:
            return "We didn't understand that, please check your input"
    else:
        return "Please double check it, can't find the word"


user_input = input("Enter word:") 
output = definer(user_input)
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)


    