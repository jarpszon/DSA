class SoftwareEngineer:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self._salary = None

    @property
    def salary(self):
        return self._salary    

    @salary.setter
    def salary(self, value):
        self._salary = value
  
se1 = SoftwareEngineer('Jarek', 25)
print(f'{se1.name} is {se1.age} old')  

se1.salary = 6000
print(se1.salary)