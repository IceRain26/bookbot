def get_book_text(file):
    with open(file) as f:
        return f.read()
    
def get_num_words(file):
    book_text = get_book_text(file)
    words = book_text.split()
    count_words = [word.strip('.,!?";:()[]') for word in words if word.strip('.,!?";:()[]')]
    print(f"Found {len(count_words)} total words")

def count_characters(file: str) -> dict:
    with open(file) as f:
        text = f.read().lower()
        char_count = {}
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

def statistics(file):
    char_count = count_characters(file)
    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    for char, count in sorted_char_count.items():
        if char.isalpha():
            print(f"{char}: {count}")
        
        
    
