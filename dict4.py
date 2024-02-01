num_students = int(input("Enter the students amount:"))
input_data = []

for i in range(num_students):
    student_info = input()
    input_data.append(student_info)
students_dict = {}
for line in input_data:
    name, number, course = line.split(":")
    students_dict[name] = {"number": int(number), "course": course}
desired_course = input()
for name, info in students_dict.items():
    if desired_course == info["course"]:
        print(f"{name} - {info['number']}")

