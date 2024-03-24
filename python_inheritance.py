class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"
    
vinay = Supervisors("Vinay", "B", "pwd")    
sushu = Chefs("Sushmitha", "B")    
juno = Employees("Juno", "J")

print(sushu.leave_request(3))
print(vinay.password)
print(vinay.name)