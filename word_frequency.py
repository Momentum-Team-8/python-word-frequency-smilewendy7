

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    

    file = open ("praise_song_for_the_day.txt") 

    text = file.read().split(" ")

    import string
    text_no_punctuation= [ word.replace(string.punctuation, "") for word in text]

    # line.translate(line.maketrans("", "", string.punctuation))

    print(text_no_punctuation)

    # text.replace (STOP_WORDS, "")

    len(text)
    text[:20]
    print(text.count('we'))
    words = set(text)

    'hello' in words
    # false

    # for loop count words 
    for word in text_no_punctuation:
        # print(word)
        print(f" {word}, {text.count(word)} ")
    return text_no_punctuation.count(word)
        



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
