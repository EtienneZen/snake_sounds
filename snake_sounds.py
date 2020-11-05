#This is my madlib generator I built for the level1tech 'devember' challange.
#I wanted to learn python and a refresh some basic coding.

# imported modules
import random

# defining madlib class
class Madlib:
    # initializing my madlib class
    def __init__(self, name, title, adverb, verb, noun, adjective, number, file_name):
        self.title = title
        self.adverb = adverb
        self.verb = verb
        self.noun = noun
        self.adjective = adjective
        self.number = number
        self.file_name = file_name

# defining madlib list
madlib_list = []

# defining instances of Madlib
zoo = Madlib ('A Day At The Zoo!', 2, 3, 3, 4, 0, 'zoo.txt')
fun = Madlib ('The Fun Park!', 2, 3, 2, 3, 1, 'fun_park.txt')

# adding class instances to a list
madlib_list.append(zoo)
madlib_list.append(fun)

# select and retrun a random item from list
selected_madlib = random.choice(madlib_list)

# begin function that introduces the player to the game and prompts them to begin
# This function will ask the user to hit enter to begin and need to return a random
# that will be used to pick a madlib later.
def begin():
    print('      \n\n\n                                    Welcome to\n')
    print('''                 ____              _            ____                        _       
               / ___| _ __   __ _| | _____    / ___|  ___  _   _ _ __   __| |___   
               \___ \| '_ \ / _` | |/ / _ \   \___ \ / _ \| | | | '_ \ / _` / __|  
                ___) | | | | (_| |   <  __/    ___) | (_) | |_| | | | | (_| \__ \   
               |____/|_| |_|\__,_|_|\_\___|___|____/ \___/ \__,_|_| |_|\__,_|___/''')
    print('\n\n                                                          By Stephen Saunders\n\n')
# intro text
    print('''                    This is a program I worte for the Level1techs 2020 Devember challenge.
                I challenged myself to learn python and build this simple program as an 
                example of what I have learned. I really enjoyed the process and could
                not have done it without all the great people at level1 cheering me on
                and answering my questions when I needed help. This is a simple madLib
                generator. After your press enter a madlib will be selected and you will
                be prompted to enter some random words.\n\n\n''')
   
    input ('                                                             Press enter to continue. . . ')

    return
def get_word(selected_madlib):
    """this function gets words for the madlib and stores them into individual lists"""
    # prints the title for the selected madlib
    print ('You will be playing', selected_madlib.title)

    # defines an empty word list
    adverb_list = []
    verb_list = []
    noun_list = []
    number_list = []

    # if class instance is empty it is skipped else it is looped into a list
    if selected_madlib.adverb == 0:
        pass
    else:
        for i in selected_madlib.adverb:
            adverb_list.append(input('Enter an adverb: '))

    # if class instance is empty it is skipped else it is looped into a list
    if selected_madlib.verb == 0:
        pass
    else:
        for i in selected_madlib.verb:
            adverb_list.append(input('Enter an verb: '))

    # if class instance is empty it is skipped else it is looped into a list
    if selected_madlib.noun == 0:
        pass
    else:
        for i in selected_madlib.noun:
            adverb_list.append(input('Enter an noun: '))

            # if class instance is empty it is skipped else it is looped into a list
            if selected_madlib.number == 0:
                pass
            else:
                for i in selected_madlib.number:
                    adverb_list.append(input('Enter an number: '))


# Used for testing
# begin ()
#print (selected_madlib.name)


# once madlib has been selected a git-word function will need to get input from a user
# This function will need to read what words it needs to git,
# print the name of the varibles it needs from the user and then
# return the varibles in a list to be inserted later.

# print_lib function will need to insert the correct varibles into the correct location
# and print the final madlib onto the screen.

# func_main
    # call begin
    # call gitword
    # call print

#profit
