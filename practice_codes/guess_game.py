from random import shuffle

mylist = [' ', '0', ' ']

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(mylist)

shuffle_list()