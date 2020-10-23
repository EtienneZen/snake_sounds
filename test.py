import string   #string module

def longest_word (text):
    """returns the longest word from a string"""
    long_word = 0
    long_word_list = text.split ()
    for i in range (long_word_list):
        if (len(i) > len(long_word))
            long_word = i
return long_word

if __name__ == "__main__":
    print(longest_word("We want a SHRUBBERY"))
