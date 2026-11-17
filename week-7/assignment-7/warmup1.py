with open('../data/notes.txt', 'r') as file:
    line_no=1
    for line in file:
        print("Line",line_no, ":", line.strip())      
        line_no += 1