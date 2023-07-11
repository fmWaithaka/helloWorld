import random
from faker import Faker


def generate_student_data():
    # Create an instance of the Faker class to generate random names
    fake = Faker()

    # Create an empty list to store the student dictionaries
    student_list = []

    # Generate data for 10 students
    for student_id in range(1, 11):
        # Generate random data for each student
        student = {
            "id": student_id,
            "name": fake.name(),  # Generate a random name using Faker
            "gender": random.choice(["Male", "Female"]),  # Randomly choose a gender
            "age": random.randint(19, 30),  # Generate a random age between 19 and 30
        }

        # Append the student dictionary to the list
        student_list.append(student)

    # Return the list of student dictionaries
    return student_list


# Delete the student given the id
def delete_student(id):
    for i in range(len(student_list)):
        if student_list[i]["id"] == id:
            del student_list[i]
            return True  # Deletion successful

    return False  # ID not found


# Generate student data
student_list = generate_student_data()

# Print the list of student dictionaries
for student in student_list:
    print(student)

# Take input from the user
entered_id = int(input("Enter id to be deleted: "))
if delete_student(entered_id):
    print("Student deleted successfully.")

    # Print the updated list of student dictionaries
    print("Updated list of students:")
    for student in student_list:
        print(student)
else:
    print("Student with entered ID not found.")
