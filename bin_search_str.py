#!/usr/bin/python3

# comparison b/w linear and binary search operations in Python
import random
import datetime


def random_file(words_dict):
    with open(words_dict) as f:
        list_words = f.readlines()
        random_word_pos = random.randint(0, len(list_words)-1)
        return random_word_pos, list_words[random_word_pos].strip()


def linear_search(list, key):
    start = datetime.datetime.now()
    """If key is in the list returns its position in the list"""
    for i, item in enumerate(list):
        if item == key:
            return i, (datetime.datetime.now() - start)


def binary_search(list, key):
    start = datetime.datetime.now()
    """If key is in the list returns nr of times list were
    halfed for binary search"""
    left = 0
    right = len(list) - 1
    nr_of_iterations = 0
    while left <= right:
        middle = (left + right) // 2

        nr_of_iterations += 1

        if list[middle] == key:
            return nr_of_iterations,  (datetime.datetime.now() - start)
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1


def main():
    words_dict = 'words.txt'
    pos, word = random_file(words_dict)
    print(f'Random word from Words.txt file: {word}')

    with open(words_dict) as words_file:
        words = [word.strip() for word in words_file]
        linear_item, linear_time = linear_search(words, word)
        binary_item, binary_time = binary_search(words, word)
        binary_factor = linear_time//binary_time

        print(f'Linear Search: {linear_item}, {linear_time}')
        print(f'Binary Search: {binary_item}, {binary_time}')
        print(f'Binary Search was : {binary_factor} times faster')


main()
