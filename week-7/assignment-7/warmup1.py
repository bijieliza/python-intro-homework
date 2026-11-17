#import os
#print(os.getcwd())
with open('../data/notes.txt', 'r') as file:
    for line in file:
        print(line.strip())      