#!/usr/bin/env python

# correcthorse.py
# Zakk Acreman
# Public domain license
# Generates passphrases of English language words

import sys, argparse, string, json
from Crypto.Random.random import randint, sample

WORD_FILE = "words.json"
WORD_LIST = json.load(open(WORD_FILE))

DEFAULTS = { 'phrases': 10,
             'words': 4,
             'length': 14,
             'separator': ' '}

parser = argparse.ArgumentParser(prog="correcthorse.py",
                                 description="Generate passphrases of English words using PyCrypto random number generator.")
parser.add_argument("num_words",
                    nargs="?",
                    default=DEFAULTS['words'],
                    type=int, 
                    help="number of words to use in the passphrase. Not including number from --addnum. Default: %(default)s")
parser.add_argument("min_length",
                    nargs="?",
                    default=DEFAULTS['length'],
                    type=int,
                    help="minimum number of characters in the passphrase. Default: %(default)s")
parser.add_argument("num_phrases",
                    nargs="?",
                    default=DEFAULTS['phrases'],
                    type=int,
                    help="number of passphrases to generate.")
parser.add_argument("-a", "--addnum",
                    action="store_true",
                    default=False,
                    help="include a randomly generated four-digit number in the passphrase." )
parser.add_argument("-c", "--caps",
                    action="store_true",
                    default=False, 
                    help="randomly capitalize or title case words.")
parser.add_argument("-s", "--separator",
                    default=DEFAULTS['separator'],
                    type=str,
                    help='character to use as separator in passphrase. Defaults to space. To randomly select between multiple separators, specify a string, like \'^b#@!\'.')

def generate_passphrases(phrases=DEFAULTS['phrases'],
                         words=DEFAULTS["words"],
                         length=DEFAULTS["length"],
                         separator=DEFAULTS['separator'],
                         addnum=False,
                         caps=False):
    passphrases = []
    for _ in range(phrases):
        passphrases.append(generate_passphrase(words, length, separator, addnum, caps))
    return passphrases

def generate_passphrase(words=DEFAULTS["words"],
                        length=DEFAULTS["length"],
                        separator=DEFAULTS['separator'],
                        addnum=False,
                        caps=False):
    phrase = []
    for _ in range(words):
        word = sample(WORD_LIST, 1)[0]
        if caps:
            if randint(0,1):
                phrase.append(word.upper())
            else:
                phrase.append(word)
        else:
            phrase.append(word)
    if addnum: 
        num = str(randint(0, 9999)).rjust(4, '0')
        phrase.insert(randint(0,len(phrase)),num)

    phrase_str = generate_phrase_str(phrase, separator)
    if len(phrase_str) >= length:
        return phrase_str
    else:
        generate_passphrase(words, length, separator, addnum, caps)

def generate_phrase_str(phrase, separator=DEFAULTS['separator']):
    phrase_str = ''
    while phrase:
        if len(phrase) == 1:
            phrase_str = phrase_str + phrase.pop(0)
        else:
            sep = sample(separator, 1)[0]
            phrase_str = phrase_str + phrase.pop(0) + sep
    return phrase_str

def print_phrases(phrases=[["something", "has", "gone", "wrong"]],
                  separator=" "):
    for phrase in phrases:
        print(phrase)

if __name__ == "__main__":
    args = parser.parse_args()

    passphrases = generate_passphrases(args.num_phrases, args.num_words, args.min_length, args.separator, args.addnum, args.caps)

    print_phrases(passphrases)
