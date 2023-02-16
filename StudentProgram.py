import StudentClass as s

def main():

    student_id = input('Enter your student id: ')
    name = input('Enter your name: ')
    dob = input('Enter your date of birth: ')
    classification = input('Enter classification (F, S, Jr, Sr): ')


    student = s.Student(id, name, dob, classification)

    student.calc_age()
    student.calc_registration_date()

    print('Your age is: ', student.get_age())
    print('Your registration dates are: ', student.get_registration_date())

main()