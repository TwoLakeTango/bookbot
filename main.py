
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)
#from stats import get_num_words
def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
main()

def get_num_words():
    book_text_words = get_book_text("books/frankenstein.txt").split()
    word_count = 0
    for word in book_text_words:
        word_count += 1
    print(f"{word_count} words found in the document")
get_num_words()
