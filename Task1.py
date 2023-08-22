from collections import Counter
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

def main():
    print("Enter the Statement: ")
    statement = input()

    repeated_chars = count_duplicates(statement)
    total_repeated_chars = len(repeated_chars)

    # Total number of characters
    total_characters = len(statement)

    # Total number of words
    words = statement.split()
    total_words = len(words)

    # Reverse characters and words
    reversed_chars = statement[::-1]
    reversed_words = ' '.join(reversed(words))

    # Form a new statement from reversed words
    new_statement = reversed_words

    # Remove duplicate characters from the new statement
    simplified_new_statement = ""
    for char in new_statement:
        if char not in simplified_new_statement:
            simplified_new_statement += char

    # Print results
    print(f"Total number of characters: {total_characters}")
    print(f"Total number of duplicate characters: {total_repeated_chars}")
    print(f"Total number of words: {total_words}")
    print(f"Reversed characters: {reversed_chars}")
    print(f"Reversed words: {reversed_words}")
    print(f"New statement from reversed words: {simplified_new_statement}")

if __name__ == "__main__":
    main()




