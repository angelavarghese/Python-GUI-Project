import json


# program to find number of recurring words in paragraph
def wordFreq(str):
    # or make list, and remove punctuation
    words = (str.lower()).split()
    # loop to remove punctuation from words
    for word in words:  # this loop goes through each word in list
        for i in range(len(word)):  # this loop goes through each index of word
            x = ord(word[i])
            # each character can only be a letter
            if x not in (range(97, 123) or range(65, 91)):
                words[words.index(word)] = word.replace(word[i], '')

    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    # printing the dictionary
    return count


def maxFreq(count):
    max = 0
    for key, value in count.items():
        if value > max:
            max = value

    for key, value in count.items():
        if count[key] == max:
            return {key: max}
