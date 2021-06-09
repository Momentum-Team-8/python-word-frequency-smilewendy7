

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    # with open(file) as the_hill_we_climb:
    #     text = the_hill_we_climb.read().lower()
    #     str = repr(text[0:-1]) 
    #     print(str)

    #     print(str.strip(".,'"))
    import re
    
    file = open ("praise_song_for_the_day.txt") 
    text = file.read().lower()
    
    # success!!! ***************************** 
    text_split= re.split("[' '\n’]", text)
    # text = file.read().split(" ")
    # print(text_split)

    ### remove STOP_WORDS in file:
    # text_no_stop= [ text.replace(for i in STOP_WORDS, "")]
    # print(text_no_stop)


    # import string

    # remove puncuation
    text_no_punctuation= [ word.strip(",.'") for word in text_split]
    # print(text_no_punctuation)
    # [ word.strip([string.punctuation]) for word in text]
    # line.translate(line.maketrans("", "", string.punctuation))

    # remove STOP_WORDS from text_no_punctuation

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # for element in STOP_WORDS:
    #     if element in text_no_punctuation:
    #         text_no_punctuation.remove(element)
        
    # print(f"stop {STOP_WORDS}")
    # print(f"text {text_no_punctuation}")
    
    # print(text_no_punctuation.remove(element))
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # print(text)
    # len(text)
    # text[:20]
    # print(text.count('we'))
    # words = set(text)

    # 'hello' in words
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
