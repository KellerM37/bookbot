def main():    
    # Define path for book
    book_path = "books/frankenstein.txt"

    text = read_book(book_path)

    print(text)

# Takes $PATH and reads book from file
def read_book(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

# Program init
main()
    