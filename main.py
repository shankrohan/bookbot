def main():
    bookPath = "books/frankenstein.txt"
    bookText = read_book(bookPath)
    print(f"Number of words: {count_words(bookText)}")
    print(f"Number of chars: {count_characters(bookText)}")

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

main()