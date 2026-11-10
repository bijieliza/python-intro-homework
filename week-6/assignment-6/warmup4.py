def is_valid_score(score):
    if score >=0 and score <= 100:
       return True
    return False
score = int(input("Enter score"))
if is_valid_score(score):
   print("valid")
else:
   print("Invalid")
