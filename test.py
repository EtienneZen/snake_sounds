import string
#loop thgat prints all combos of two letters of the alphabet
for i in string.ascii_lowercase:
    for x in string.ascii_lowercase:
        if i == x:
            pass
        else:
            print (i+x)
