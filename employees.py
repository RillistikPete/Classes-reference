class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name):
        self.name = name

    #this allows you to add a set of employees to the specific company (Company.employees)
        self.employees = set()

    def get_name(self):
        """Returns the name of the company"""
        return self.name

    # Add the remaining methods to fill the requirements above

class Employee:
    def __init__(self, firstName = "", lastName = "", employeeID = ""):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID


# Add employees to a company once you make a company

PeteCompany = Company("PeteCompany")

pete = Employee("Pete", "Swayze", "123456")
chris = Employee("Chris", "Bomb", "012345")
chad = Employee("Chad", "Brown", "001234")
#Chris showed me you can do it this way too since you made 'firstName = "" ' for example
steve = Employee()
steve.firstName = "Steve"
steve.lastName = "Brownlee"
steve.employeeID = "098"

PeteCompany.employees.add(pete)
PeteCompany.employees.add(chris)
PeteCompany.employees.add(chad)
PeteCompany.employees.add(steve)

for e in PeteCompany.employees:
    print(e.firstName)