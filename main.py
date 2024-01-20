def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_freq = get_char_freq(text)
    char_freq_list = [(key, value) for key, value in char_freq.items() if key.isalpha()]
    char_freq_list_sorted = sorted(char_freq_list, key = lambda letter : letter[1], reverse = True)
    print(f"\n--- Report of {book_path} ---\n")
    print(f"There are {num_words} words in this document\n")
    print("The frequency of each character: \n")
    for char, value in char_freq_list_sorted:
        print(f"The letter \"{char}\" appears {value} times")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_freq(text):
    char_freq_dict = {}
    for char in text.lower():
        if char in char_freq_dict:
            char_freq_dict[char] += 1
        else:
            char_freq_dict[char] = 1
    return char_freq_dict
main()
