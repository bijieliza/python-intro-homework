students= [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

highest_score = 0
topscorer = ""
class_avg=0
for student in students:
    if student["score"] > highest_score:
        highest_score =student["score"]
        topscorer = student["name"]
        
print(f"Topscorer:  {topscorer} ({highest_score})")

for student in students:
     class_avg  += student["score"]/len(students)
print(f"Class average: {class_avg}")

subject=set()
for student in students:
     subject.add(student["subject"])
print(f"Subjects offered: {subject}")
highscorers=[]
for student in students:
     if student["score"] > 75:
        highscorers.append(student["name"])
print(f"High scorers: {highscorers}")


