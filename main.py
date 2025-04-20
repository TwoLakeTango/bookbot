def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

from stats import get_num_words
from stats import character_frequency

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text[:100])

main()

word_count = get_num_words()
character_dict = character_frequency()
