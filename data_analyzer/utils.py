import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/tags.csv', 'r') as f:
    reader = csv.reader(f)

    tags_rating = list(reader)

with open(dir_path+'/words.txt') as word_dictionary:
    dict_words = {x.rstrip().lower() for x in word_dictionary.readlines()}

tags = {tag for (tag, _) in tags_rating}



def get_non_dict_word(words_set):
        non_word = words_set - (dict_words & words_set)
        return non_word

def get_tags_from_word_set(word_set):
    return tags & word_set