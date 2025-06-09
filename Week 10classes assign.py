import re

# class of validator
class Validator:
    @staticmethod
    def validate_student_id(student_id):
        return student_id.isdigit() and len(student_id) <= 7

    @staticmethod
    def validate_name(name):
        return bool(re.match(r"^[A-Za-z\s'-]+$", name))

    @staticmethod
    def validate_email(email):
        return bool(re.match(r"^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email))

    @staticmethod
    def validate_program(program):
        return len(program.strip()) > 0

    @staticmethod
    def validate_instructor_id(instructor_id):
        return instructor_id.isdigit() and len(instructor_id) <= 5

    @staticmethod
    def validate_institution(institution):
        return len(institution.strip()) > 0

    @staticmethod
    def validate_degree(degree):
        return len(degree.strip()) > 0


# Individual class
class Individual:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInformation(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


# Student class
class Student(Individual):
    def __init__(self, name, email, student_id, program):
        super().__init__(name, email)
        self.student_id = student_id
        self.program = program

    def displayInformation(self):
        super().displayInformation()
        print(f"Student ID: {self.student_id}")
        print(f"Program: {self.program}")


# Instructor class
class Instructor(Individual):
    def __init__(self, name, email, instructor_id, institution, degree):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.institution = institution
        self.degree = degree

    def displayInformation(self):
        super().displayInformation()
        print(f"Instructor ID: {self.instructor_id}")
        print(f"Last Institution: {self.institution}")
        print(f"Highest Degree Earned: {self.degree}")


# Collecting  the records
college_records = []

def get_valid_input(prompt, validation_func):
    while True:
        data = input(prompt)
        if validation_func(data):
            return data
        print("Invalid input. Please try again.")

while True:
    person_type = input("Is the individual a student or an instructor? (student/instructor): ").strip().lower()
    if person_type not in ['student', 'instructor']:
        print("Please enter 'student' or 'instructor'.")
        continue

    name = get_valid_input("Enter name: ", Validator.validate_name)
    email = get_valid_input("Enter email: ", Validator.validate_email)

    if person_type == 'student':
        student_id = get_valid_input("Enter Student ID (up to 7 digits): ", Validator.validate_student_id)
        program = get_valid_input("Enter program of study: ", Validator.validate_program)
        student_obj = Student(name, email, student_id, program)
        college_records.append(student_obj)
    else:
        instructor_id = get_valid_input("Enter Instructor ID (up to 5 digits): ", Validator.validate_instructor_id)
        institution = get_valid_input("Enter last institution graduated from: ", Validator.validate_institution)
        degree = get_valid_input("Enter highest degree earned: ", Validator.validate_degree)
        instructor_obj = Instructor(name, email, instructor_id, institution, degree)
        college_records.append(instructor_obj)

    cont = input("Do you want to enter another individual? (yes/no): ").strip().lower()
    if cont != 'yes':
        break

# Print the college  records
print("\n--- College Records ---")
for record in college_records:
    record.displayInformation()
    print("------------------------")