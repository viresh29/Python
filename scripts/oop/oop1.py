# position, name, age, level, salary


se1 = ['Software Engineer', 'Max', 20, "Junior", 5000]
se2 = ['Software Engineer', 'Lisa', 25, "Senior", 7000]

# class


class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0
    # getter

    def get_salary(self):
        return self._salary
    # setter

    def set_salary(self, value):
        # check value
        if value < 1000:
            self._salary = 1000
        elif value > 20000:
            self._salary = 20000
        else:
            self._salary = value


se = SoftwareEngineer("Max", 25)
se.set_salary(50000)
print(se.get_salary())
# class Employee:

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def work(self):
#         print(f'{self.name} is working')


# class SoftwareEngineer(Employee):
#     pass

# # class attributes
# alias = 'Keyboard Musician'

# def __init__(self, name, age, level, salary) -> None:
#     # instance attributes
#     self.name = name
#     self.age = age
#     self.level = level
#     self.salary = salary

# def code(self):
#     print(f"{self.name} is writing code ...")

# def code_in_language(self, language):
#     print(f"{self.name} is writing code in {language}")

# def information(self):
#     information = 'Hi'
#     return information


# class Designer(Employee):
#     pass


# se = SoftwareEngineer("Max", 20)
# print(se.name)
# print(se.age)
# se.work()
# # instance of class
# # se1 = SoftwareEngineer('Max', 20, "Junior", 5000)
# # print(se1.name, se1.age)
# # print(SoftwareEngineer.alias)
# # print(se1.code())
# # print(se1.code_in_language('Java'))
# # print(se1.information())
# # Recap
# # create a class (blueprint)
# # create a instance
# # class vs instance
# # instance attributes: defined in __init__(self)
# # class attributes
