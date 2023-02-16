from datetime import date

class Student:

    def __init__(self, id, name, dob, classification):
        self.__student_id = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__registration_date = ''
    

    def calc_age(self):
        today = date.today()
        year = today.year
        
        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        self.__age = year - dob_year
    

    def calc_registration_date(self):
        if self.__classification == 'F':
            self.__registration_date = '4/10 through 4/12'
        elif self.__classification == 'S':
            self.__registration_date = '4/7 through 4/9'
        elif self.__classification == 'Jr':
            self.__registration_date = '4/4 through 4/6'
        elif self.__classification == 'Sr':
            self.__registration_date = '4/1 through 4/3'
        else:
            self.__registration_date = 'classification not found'


    def get_age(self):
        return self.__age
    
    
    def get_registration_date(self):
        return self.__registration_date
