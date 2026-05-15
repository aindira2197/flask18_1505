class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print("Universitet:", self.name)

        for student in self.students:
            print(student)

uni = University("TATU")

uni.add_student("Ali")
uni.add_student("Vali")
uni.add_student("Sami")

uni.show_students()
