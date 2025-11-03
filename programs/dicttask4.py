students = [
      {"id": 1, "name": "John", "marks": {"math": 80, "science": 75}},
      {"id": 2, "name": "Jane", "marks": {"math": 90, "science": 85}}
  ]


for student in students:
    print(student['name'])
    #print(student['marks'])
    for subject,marks in student['marks'].items():
        print(subject.ljust(10),marks)
    print("-------------------")

