from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_book_characters(text)
    char_report = get_char_report(char_dict)
    
    # Print report Header
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    # Print each line in the character report
    for character, count in char_report:
        if character.isalpha(): #Ensures only alphabetic characters are reported.
            print(generate_report_line(character, count))

    # Print report footer
    print(f"--- End report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_characters(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

#Lambda is a single use function that takes a single argument aka item here.
def get_char_report(char_dict):
    report_items = list(char_dict.items())  # Convert to a list of tuples 
    report_count = sorted(report_items, key=lambda item: item[1], reverse=True)
    return report_count

def  generate_report_line(character, count):
    return f"The '{character}' character was found {count} times"

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()