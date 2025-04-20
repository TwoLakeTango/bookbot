def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

def get_num_words():
    book_text_words = get_book_text("books/frankenstein.txt").split()
    word_count = 0
    for word in book_text_words:
        word_count += 1
    print(f"{word_count} words found in the document")

def character_frequency():
    book_text_lower = get_book_text("books/frankenstein.txt").lower()
    #unique_characters_list = []
    unique_character_count_dict = {}
    for character in book_text_lower:
      if character not in unique_character_count_dict:
        #unique_character_count_dict.append(character)
        unique_character_count_dict[character] = 1
      else:
        unique_character_count_dict[character] += 1
    #print(book_text_characters[:8])
    #print(unique_character_count_dict)    
    print(unique_character_count_dict)