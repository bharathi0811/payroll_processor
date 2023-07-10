class Calculate_pay:
    @staticmethod
    def calculate_pay(employee):
        if isinstance(employee, salaried_employee):
            return employee.calculate_pay()
        elif isinstance(employee, hourlyemployee):
            return employee.calculate_pay()
        else:
            raise ValueError("Invalid employee type")

class Employee:
    def __init__(self,name):
        self.name = name

class salaried_employee(Employee):
    def __init__(self,name,salary):
        super().__init__(name)
        self.name = name
        self.salary = salary
    def calculate_pay(self):
        return self.salary
class hourlyemployee(Employee):
    def __init__(self,name, hourlyrate,hourlyworked):
        super().__init__(name)
        self.name = name
        self.hourlyrate= hourlyrate
        self.hourlyworked = hourlyworked
        
    def calculate_pay(self):
        return self.hourlyrate*self.hourlyworked


siva = salaried_employee("siva",100000)

kannan = hourlyemployee("kannan",10,20)
print(Calculate_pay.calculate_pay(siva))
print(Calculate_pay.calculate_pay(kannan))

