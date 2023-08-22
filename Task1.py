def count_duplicates(statement):
    char_count = {}
    repeated_chars = []

    for char in statement:
        if char != ' ':
            if char in char_count:
                char_count[char] += 1
                if char_count[char] == 2:
                    repeated_chars.append(char)
            else:
                char_count[char] = 1

    return repeated_chars

def count_duplicate_words(words):
    word_count = {}
    duplicate_word_count = 0

    for word in words:
        if word in word_count:
            word_count[word] += 1
            if word_count[word] == 2:
                duplicate_word_count += 1
        else:
            word_count[word] = 1

    return duplicate_word_count

def main():
    try:
        print("Enter the Statement: ")
        statement = input()
        
        if len(statement) == 0:
            print("The input cannot be empty")
        else:
            repeated_chars = count_duplicates(statement)
            total_repeated_chars = len(repeated_chars)

            words = statement.split()
            total_words = len(words)

            duplicate_word_count = count_duplicate_words(words)

            reversed_chars = statement[::-1]
            reversed_words = ' '.join(reversed(words))

            new_statement = reversed_words
            simplified_new_statement = ""
            for char in new_statement:
                if char not in simplified_new_statement:
                    simplified_new_statement += char

            print(f"Total number of characters: {len(statement)}")
            print(f"Total number of duplicate characters: {total_repeated_chars}")
            print(f"Total number of words: {total_words}")  
            print(f"Total number of duplicate words: {duplicate_word_count}")
            print(f"Reversed characters: {reversed_chars}")
            print(f"Reversed words: {reversed_words}")
            print(f"New statement from reversed words: {simplified_new_statement}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
