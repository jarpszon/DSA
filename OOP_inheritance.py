

#base class can be inherited, extended , overriden
class Employee:
    
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working.')


#child classes
class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, salary, level) -> None:
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f'{self.name} is debugging')

    #override work function in Employee class
    def work(self):
        print(f'{self.name} is working with the code.')


class Designer(Employee):

    def draw(self):
        print(f'{self.name} is drawing')

    #override work function in Employee class
    def work(self):
        print(f'{self.name} is working on drawing.')

se1 = SoftwareEngineer('Jarek',25, 5000, 'Senior')
print(se1.name, se1.age, se1.salary, se1.level)
se1.work()
se1.debug()

d1 = Designer('Iwona',23,10000)
print(d1.name, d1.age, d1.salary)
d1.work()
d1.draw()
