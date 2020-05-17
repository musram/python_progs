class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')
class ManagerRole:
    def work(self, hours):
        print('{} screams and yells for {} hours.'.format(self.name, hours))

class SecretaryRole:
    def work(self, hours):
        print('{} expends {} hours doing office paperwork.'.format(self.name, hours))

class SalesPersonRole:
    def work(self, hours):
        print('{} expends {} hours on the phone.'.format(self.name, hours))

class FactoryWorkerRole:
    def work(self, hours):
        print('{} manufactures gadgets for {} hours.'.format(self.name, hours))    
