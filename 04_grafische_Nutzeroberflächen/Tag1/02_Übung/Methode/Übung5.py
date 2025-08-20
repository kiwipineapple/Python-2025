class Student:
    school_name = 'St Martin Gymnasium'

    @classmethod
    def class_method(cls, given_name: str):
        cls.school_name = given_name


new_school = Student
new_school.class_method('Luis Anna Gymnasium')
print(new_school.school_name)
