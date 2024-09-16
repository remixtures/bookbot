def count_words(text):
    """Returns the number of words in the given text."""
    # Split the text by whitespace and return the length of the resulting list
    words = text.split()
    return len(words)

def count_characters(text):
    """Returns a dictionary with the count of each character in the given text."""
    # Convert the text to lowercase to avoid case differences
    text = text.lower()
    
    frequency = {}
    for char in text:
        if char.isalnum():  # ignore non-alphanumeric characters
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


def print_report(word_count, char_count):
    """
    Prints a report of the word count and character frequencies.
    """
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("The top 20 most frequent characters:")
    count_chars_list = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char, freq in count_chars_list:
        print(f"The '{char}' character was found {freq} times")
    print("--- End report ---")

def main():
    # Open the file and read its contents
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    
    # Print the contents to the console
    print(file_contents)

    # Count the number of words and print the result
    word_count = count_words(file_contents)
    print("\nTotal number of words in the book:", word_count)

    # Count the occurrences of each character and print the result
    char_count = count_characters(file_contents)
    print_report(word_count, char_count)	

# Call the main function to execute the program
if __name__ == "__main__":
    main()
