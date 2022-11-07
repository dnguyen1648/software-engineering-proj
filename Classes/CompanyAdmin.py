import User
import SecurityChange


class CompanyAdmin(User):  # subclass of user for admin website

    employee_change = [0, ""] # this will hold a request to edit employee data to be passed to website controller
    # 0- view, 1- add, 2- edit, 3- delete, with the second element of the list being the argument/target
    sec_change = SecurityChange()

    def create_security_change(self):
        # this will make a new security options change
        pass

    def pass_security_change(self, sec_change):
        # this will pass the security change to the website controller
        pass

    def pass_employee_change(self, employee_change):
        # this will pass the employee change to the website controller
        pass
