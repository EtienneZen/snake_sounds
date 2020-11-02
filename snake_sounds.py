#This is my madlib generator I built for the level1tech 'devember' challange.
#I wanted to learn python and a refresh some basic coding.

    #imported modules

#I think I will need to define a class here for the madlibs
# madlib txt should be stored in a seperate file

#begin function that introduces the player to the game and prompts them to begin
#This function will ask the user to hit enter to begin and need to return a random 
#that will be used to pick a madlib later.
def begin():
    print('      \n\n\n                                    Welcome to\n')
    print('''                 ____              _            ____                        _       
               / ___| _ __   __ _| | _____    / ___|  ___  _   _ _ __   __| |___   
               \___ \| '_ \ / _` | |/ / _ \   \___ \ / _ \| | | | '_ \ / _` / __|  
                ___) | | | | (_| |   <  __/    ___) | (_) | |_| | | | | (_| \__ \   
               |____/|_| |_|\__,_|_|\_\___|___|____/ \___/ \__,_|_| |_|\__,_|___/''')
    print('\n\n                                                          By Stephen Saunders\n\n')
                #intro text
    print('''                    This is a program I worte for the Level1techs 2020 Devember challenge.
                I challenged myself to learn python and build this simple program as an 
                example of what I have learned. I really enjoyed the process and could
                not have done it without all the great people at level1 cheering me on
                and answerng my questions when I needed help. This is a simple madLib
                generator. After your press enter a madlib will be selected and you will
                be prompted to enter some random words.\n\n\n''')
   
    input ('                                                             Press enter to continue. . . ')
    #rando lib here
    return
   

begin() #used for testing
    





#once madlib has been selected a git-word function will need to get input from a user
#This function will need to read what words it needs to git,
#print the name of the varibles it needs from the user and then 
#return the varibles in a list to be inserted later.

#print_lib function will need to insert the correct varibles into the correct location 
#and print the final madlib onto the screen.

#func_main
    #call begin
    #call gitword
    #call print

#profit
