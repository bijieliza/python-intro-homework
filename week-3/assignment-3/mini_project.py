day=input("What day is it? ")
time=input("What time of day? ")
if day.lower() == "monday" :
    if time.lower() == "morning":
        print("Suggestion: Morning Python class — great time to focus!")
    elif time.lower() == "afternoon":
        print("Suggestion:Perfect Afternoon for a mentor session!.")
    elif time.lower() == "evening":
        print("Suggestion: Perfect evening to take Code The Dream Quiz.")
    else:
        print("Sorry, I don't recognize that time. Try: Morning, Afternoon, Evening...")
elif day.lower() ==  "tuesday":
    if time.lower() == "morning":
        print("Suggestion: Morning Python class — great time to focus!")   
    elif time.lower() == "afternoon":
        print("Suggestion:Perfect afternoon for doing the assignment.!")
    elif time.lower() == "evening":
        print("Suggestion: Perfect evening to submit the assignment.")
    else:
         print("Sorry, I don't recognize that time. Try: Morning, Afternoon, Evening...")
elif day.lower()== "wednesday" :
    if time.lower() == "morning":
        print("Suggestion: Morning Python class — great time to focus!")   
    elif time.lower() == "afternoon":
            print("Suggestion:Perfect Afternoon for trying a new recepie.!")
    elif time.lower() == "evening":
            print("Suggestion: Perfect evening for a movie.")
    else:
         print("Sorry, I don't recognize that time. Try: Morning, Afternoon, Evening...")
else:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")

