#What day is it? Tuesday
#What time of day? morning
#Suggestion: Morning Python class — great time to focus!
day=input("What day is it? ")
time=input("What time of day? ")
if day.lower() == "monday" and time == "morning":
    print("Suggestion: Morning Python class — great time to focus!")
elif day.lower() == "monday" and time == "afternoon":
    print("Suggestion:Perfect Afternoon for a mentor session!.")
elif day.lower() ==  "monday" and time == "evening":
    print("Suggestion: Perfect evening to take Code The Dream Quiz.")
elif day.lower() ==  "tuesday"and time == "morning":
    print("Suggestion: Morning Python class — great time to focus!")   
elif day.lower() ==  "tuesday" and time == "afternoon":
    print("Suggestion:Perfect afternoon for doing the assignment.!")
elif day.lower() ==  "tuesday" and time == "evening":
    print("Suggestion: Perfect evening to submit the assignment.")
elif day == "Wednesday" or "wednesday" and time == "morning":
    print("Suggestion: Morning Python class — great time to focus!")   
elif day.lower() ==  "wednesday" and time == "afternoon":
    print("Suggestion:Perfect Afternoon for trying a new recepie.!")
elif day.lower() ==  "wednesday" and time == "evening":
    print("Suggestion: Perfect evening for a movie.")
else:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")



