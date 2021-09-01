se1 = ['Software engineer','Jarek', 25, 'Senior', 1000]
se2 = ['Software engineer','Iwona', 23, 'Junior', 2000]


class SoftwareEngineer:

    #class attribute
    alias = "keyboard magician"
 
    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    #__str__ defines what is when you print object/instance itself
    def __str__(self) -> str: 
        return f'name = {self.name}, age = {self.age}'

    # __eq__ checks the memory address so we replace it with our own definition
    def __eq__(self, o: object) -> bool:
        return self.name == o.name and self.age == o.age
    
    #class method
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


    #instance method
    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}...')

    def information(self):
        info = f'name = {self.name}, age = {self.age}'
# instance

se3 = SoftwareEngineer('Max', 25, 'Senior', 1000)
se4 = SoftwareEngineer('Max', 24, 'Senior', 10000)
print(se3.name, ' ' , se3.age)
print(se3.alias)
print(SoftwareEngineer.alias)
se3.code()
se3.code_in_language('Polish')
print(se3)
print(se3==se4)

print(se3.entry_salary(se3.age))
print(SoftwareEngineer.entry_salary(se4.age))