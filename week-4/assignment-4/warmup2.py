student={"name": "Mini", "score": 78, 
         "subject": ["Math","Science","English"]}
for key, value in student.items():
    print(f"{key}: {value}")
student["graduated"]=False
print(student)