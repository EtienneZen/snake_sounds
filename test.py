import string   #string module

def longest_word (text):
    """converts to a list and returns the longest word word from the list"""
    return max(text.split (), key=len)

#used for testing
if __name__ == "__main__":
    print(longest_word("""The for statement is a tool
    to traverse things containing items. Strings, lists, and ranges are things containing items,
    so you can use a for to iterate their elements, like:"""))
