class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print('Payroll for: {} - {}'.format(employee.id, employee.name))
            print('- Check amount: {}'.format(employee.calculate_payroll()))
            print('')
'''
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
'''

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass

        

    class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission



if __name__ == "__main__":



    #While you can instantiate an Employee object, the object cant be used by the PayrollSystem. Why? Because it cant .calculate_payroll() for an Employee.
    '''
    employee = Employee(1, "Invalid")
    payroll_system = PayrollSystem()
    payroll_system.calculate_payroll([employee])
    '''
    
    #Cant instantiate a abstractclass
    employee = Employee(1, "Invalid")    
    
    
