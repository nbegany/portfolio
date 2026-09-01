'''
This program is created to gather employee information.
In addition, if the employee is a manger it asks for
further information. And, it asks if the manager would
like to be on the mailing list. Then, it displays
the employee's or manager's information. 
Steps:
1. create employee class
2. create __init method for employee
3. create set methods for employee
4. create get methods for employee
5. create __str__ method for employee
6. create manager subclass
7. create __init__ method for manager subclass
8. create set methods for manager
9. create get methods for manager
10. create __str__ method  for manager
11. define the main function
12. ask for employee information and if the employee
is a manager
13. if the employee is not a manager, create employee object,
and display employee information
14. if the employee is a manager, create manger object,
and display manager information
'''

# create class employee
class Employee:

    # create __init__ method for employee
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone
    
    # create set methods for employee
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__telephone = telephone
    
    # create get methods for employee
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone

    #  create __str__ method for employee
    def __str__(self):
        return ("Employee Name: " + self.__name + \
                "Address: " + self.__address + \
                "Telephone Number: " + self.__telephone)

# create manager subclass
class Manager(Employee):

    # create __init__ method for manager subclass
    def __init__(self, name, address, telephone, manager_num, maillist):

        # call superclass __init__
        Employee.__init__(self, name, address, telephone)

        self.__manager_num = manager_num
        self.__mail = maillist
        
    # create set methods for manager 
    def set_manager_num(self, manager_num):
        self.__manager_num = manager_num

    def set_mail(self, maillist):
        self.__mail = maillist

    # create get methods for manager 
    def get_manager_num(self):
        return self.__manager_num

    def get_maillist(self):

        if self.__mail.upper() == 'Y':
            return "You are included in the mailing list!"

        else:
            return "You are not included in the mailing list!"

    # create __str__ method  for manager
    def __str__(self):

        return ("Manager Number: " + self.__manager_num + \
                "Mail Status: " + self.get_maillist())

# define main function
def main():

    # ask for employee information
    print("Enter Employee Information")

    name = input("Enter employee name: ")
    address = input("Enter employee address: ")
    telephone = input("Enter employee telephone number: ")

    # ask if employee is a manager
    manager_choice = input("Is this employee a manager? (Y/N): ")

    # if employee is not a manager
    if manager_choice.upper() == 'N':

        # create employee object
        myEmployee = Employee(name, address, telephone)

        # display information using get methods
        print("--------------------")
        print("EMPLOYEE INFORMATION")
        print("Name:", myEmployee.get_name())
        print("Address:", myEmployee.get_address())
        print("Telephone:", myEmployee.get_telephone())

    # if employee is a manager
    else:

        # ask for manager information
        manager_num = input("Enter manager number: ")
        maillist = input("Would the manager like to be on the mailing list? (Y/N): ")

        # create manager object
        myManager = Manager(name, address, telephone, manager_num, maillist)

        # display manager information using get methods
        print("--------------------")
        print("MANAGER INFORMATION")
        print("Name:", myManager.get_name())
        print("Address:", myManager.get_address())
        print("Telephone:", myManager.get_telephone())
        print("Manager Number:", myManager.get_manager_num())
        print("Mail Status:", myManager.get_maillist())

# call main function
main()
