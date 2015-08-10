# Correcthorse.py

Zachary Acreman

## What is it
A simple python script to generate passphrases in the style of
[xkcd](https://www.xkcd.com/936/).

It uses pyCrypto for cryptographically sound random number
generation. 

## How to use it
From the command line,

    python correcthorse.py

will print 10 4-word passphrases.

Additionally, it is possible to specify the number of words in the
phrase, minimum length of the phrase, the number of phrases generated,
whether the phrase includes an additional number, and a selection of
additional separators for the script to use between phrase words.

These additional options are described in

    python correcthorse.py -h

## Caveats

Correcthorse.py has only been tested with Python 3.

## Acknowledgements

The word list in words.json is a derivative of the
[match 10 list](https://www.keithv.com/software/wlist/) by Keith
Vertanen.
