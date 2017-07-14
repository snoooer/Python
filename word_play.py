#!/usr/bin/env python

def count_letter(word,letter):
    for w in word:
        if w == letter:
            return False
    return True

print(count_letter('abc','c'))

def letter_pec(fin,letter):
    n_word,n_letter = 0,0
    for line in fin:
        word = line.strip()
        count = 0
        for w in word:
            if w == letter:
                count += 1
        if count != 0 :
            n_letter += 1
        n_word += 1
    return str((n_letter / n_word) * 100) + '%'


fin = open('words.txt')

print(letter_pec(fin,'z'))
fin.close()