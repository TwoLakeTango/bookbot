def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text[:100])
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

from stats import get_num_words
from stats import character_frequency
from stats import bookbot_output

word_count = get_num_words()
unique_character_count_dict = character_frequency()
dict_list = bookbot_output(unique_character_count_dict)

print("============ BOOKBOT ============\n""Analyzing book found at books/frankenstein.txt...\n""----------- Word Count ----------")
print(f"Found {word_count} total words")
print("----------- Character Count -----------")
for i in dict_list:
    character = i["character"]
    count = i["count"]
    if character.isalpha():
        print(f"{character}: {count}")
print("============= END ===============")

main()