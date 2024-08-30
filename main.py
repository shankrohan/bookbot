from operator import itemgetter

def main():
    bookPath = "books/frankenstein.txt"
    bookText = read_book(bookPath)
    numWords = count_words(bookText)
    numChars = count_characters(bookText)

    #sort count from greatest to least
    myKeys = list(numChars.keys())
    myKeys.sort()
    sorted_numChars = {i: numChars[i] for i in myKeys}

    #output to file
    outputFile = open('textInfo.txt', 'w')
    outputFile.write(f"--- Begin report of {bookPath} ---")
    outputFile.write(f"{numWords} words found in document\n")
    #print(f"--- Begin report of {bookPath} ---")
    #print(f"{numWords} words found in document\n")
    for c in sorted_numChars:
        if c.isalpha() is False:
            continue
        outputFile.write(f"The {c} character was found {sorted_numChars[c]} times!\n")

def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    lowerCaseBook = book.lower()
    characterCounter = dict()
    for c in lowerCaseBook:
        if c not in characterCounter:
            characterCounter[c] = 1
        else:
            characterCounter[c] += 1
    return characterCounter

def sort_on(dict):
    return dict[int]



main()