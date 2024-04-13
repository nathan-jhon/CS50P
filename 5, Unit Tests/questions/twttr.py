def main():
    # Example usage
    word = input("Enter a word: ")
    shortened_word = shorten(word)
    print(shortened_word)


def shorten(word):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in word if char not in vowels)


if __name__ == "__main__":
    main()

