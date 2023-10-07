import random

students = ["Alexandra", "Alexander", "Blagoy", "Vasil", "Vasilena", "Veronika", "Veselin", "viktoria", "Galya","Georgi","Daniel","Denislav","Dimitar","Zdravko","Ivelin","izabela","Joan","Jordan","Kaloyan","Krisitan","Martin","Plamen","Preslav","Rosen","Simona","Stoyan","Tsvetan1","Tsvetan2"]


def choose_random_student(students):
    if not students:
        print("No students left")
        return None
    chosen_student = random.choice(students)
    students.remove(chosen_student)
    return chosen_student

while True:
    input("Press Enter to get the next student : ")
    chosen_student = choose_random_student(students)
    if chosen_student:
        print(f"The lucky one is: {chosen_student}")
        
    
    




