#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

newlist = []
w1 = input("enter a word")
w2= input("enter a word")
w3 = input("enter a word")
w4 = input("enter a word")
w5 = input("enter a word")

newlist.append(w1)
newlist.append(w2)
newlist.append(w3)
newlist.append(w4)
newlist.append(w5)

print(newlist)

