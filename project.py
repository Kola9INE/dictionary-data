import json
from difflib import *

def retrieve(value:str):
    if value.lower() not in words:
        likely_words = get_close_matches(value, words, n = 10)
        print("\nWe cannot find the meaning of that word!\nHowever, we found matches for the word you may have meant to type. See below: \n")
        for sn, matches in enumerate(likely_words, 1):
            yield(sn, matches)
    elif value.lower() in words:
        try:
            print(f'\nThe meaning of {value.upper()} is/are:\n')
            meaning = data.get(value)
            for sn, meanings in enumerate(meaning, 1):
                yield(sn, meanings)
        except:
            print('\nWe cannot locate that word! Try searching another word!\n')
    else:
        print('Errr... Something went wrong.')
    
if __name__ == '__main__':
    # Load the JSON file. It loads it as a python dictionary
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Get the words of the dictionary in a list
    words = [word.lower() for word in data.keys()]

    word = input('\nEnter the word or phrase you are looking for here!:   ').lower().strip()
    for i, v in retrieve(word):
        print(i, v)