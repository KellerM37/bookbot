'''
BookBot
Author: KellerM37
This project is for a Boot.dev course.
'''
def main():    
    # Define path for book
    book_path = "books/frankenstein.txt"

    text = read_book(book_path)

    wc = count_words(text)

    chars = count_chars(text)

    sorted_chars = sort_chars(chars)

    create_report(book_path, wc, sorted_chars)


# Takes $PATH and reads book from file
def read_book(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

# Takes text from the book, splits at whitespace and then counts the words before returning the count
def count_words(text):
    word_count = 0
    raw_words = text.split()
    for w in raw_words:
        word_count += 1
    return word_count

# Takes text from the book, lowers the case, checks if a given character is in the dictionary AND is alphanumeric. If it is, it increments by 1. If it is not, we add it to the dictionary and set the value to one. We then return the count
def count_chars(text):
    char_count = {}
    lowercase = text.lower()
    for w in lowercase:
        if w in char_count and w.isalpha():
            char_count[w] += 1
        elif w not in char_count and w.isalpha():
            char_count[w] = 1
    return char_count

# Tell the next function (sort_chars) to sort by the count
def sort_on(x):
    return x["count"]

# Takes the dict from count_chars, converts the dict to a list of dicts and sorts it before we then send back the sorted list
def sort_chars(chars):
    sorted_list = []
    for c in chars:
        sorted_list.append({"char": c, "count": chars[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# Collects required information and prints a report showing title, word count, and # of occurences of each letter from most common to least
def create_report(path, wc, chars):
    print(f'--- Begin report for {path} ---')
    print(f'{wc} words found in the book')
    print("----------------------------------------------")
    for c in chars:
        print(f"The '{c["char"]}' was found {c["count"]} times")
    print("--- End report ---")
    return None

# Program init
main()
    