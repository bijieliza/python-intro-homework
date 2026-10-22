student={"name": "Mini", "grade": 78, 
         "subjects": ["Math","Science","English"]}
for key, value in student.items():
    print(f"{key}: {value}")
student["graduated"]=False
print(student)