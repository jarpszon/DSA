

class SoftwareEngineer:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        #PEP8 convention  protected atr stars with '_' and prrivate with '__'
        self._salary = None
        self._num_bugs_solved = 0 

    def code(self):
        self._num_bugs_solved += 1

    #getters
    def get_salary(self):
        return self._salary    

    #setters
    def set_salary(self, value):
        self._salary = self._calculate_salary(value)
  
    def _calculate_salary(self, base_salary):
        if self._num_bugs_solved < 10:
            return base_salary
        if self._num_bugs_solved <100:
            return base_salary * 2
        return base_salary * 3

se1 = SoftwareEngineer('Jarek',25)
for i in range(70):
    se1.code()

print(se1._num_bugs_solved)

se1.set_salary(5000)
print(se1.get_salary()  )

