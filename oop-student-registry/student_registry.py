class Student:
    def __init__(self, name, age = 13, grade = 12):
        self._name = name
        self._age = age
        self._grade = grade
    
    @property
    def name(self):
        return self._name.capitalize()
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
            self._name = new_name
        else:
            print("Name must be at least 3 characters.")

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            print("Age must be an integer.")
            
    @property
    def grade(self):
        return f"{self._grade}th"
    
    @grade.setter
    def grade(self, new_grade = 12):
        if isinstance(new_grade, int):
            self._grade = new_grade
        else:
            print("Grade must be no higher than 12th")

