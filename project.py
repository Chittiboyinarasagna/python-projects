class Employe:

    def __init__(self,emp_id,emp_name,emp_hourlywage):

        self.emp_id=emp_id

        self.emp_name=emp_name

        self.emp_hourlywage=emp_hourlywage

        

#printing the details of the employees

    def details(self):

        print("Id: ",self.emp_id)

        print("Name: ",self.emp_name)

        print("Hourly Salary: ",self.emp_hourlywage)

        print("--------------------------------------------")



employees={}  #dictionary to store the employee details

def create_employee(emp_id,emp_name,emp_hourlywage):

    if emp_id not in employees:

        new_employee=Employe(emp_id,emp_name,emp_hourlywage)

        employees[emp_id]=new_employee

        print("saved",emp_name,"as a new employee")

    else:

        print("Employee",emp_id,"is already existing")



#seeing the details of employees

def show_employees():

    for emp_id in employees:

        employe=employees[emp_id]  

        employe.details()



#updating the employee details



def update_employee(emp_id,new_name,new_hourlywage):

    if emp_id in employees:

        employee=employees[emp_id]

        if new_name and new_hourlywage:

            employee.emp_name=new_name

            employee.emp_hourlywage=new_hourlywage

            print("Employee with",emp_id,"is updated")

        else:

            print("inavalid name and hourly wages")

    else:

        print("employee with",emp_id,"does not exit")





#deleting the employee details frrom the dictionary



def delete_employee(emp_id):

    if emp_id in employees:

        del employees[emp_id]

        print("Successfully deleted the employee",emp_id)

    else:

        print("Employee id", emp_id,"is not found")



#printing the salary of the employee



def emp_salary(emp_id):

    if emp_id in employees:

        employee=employees[emp_id]

        salary=(25*8)+employee.emp_hourlywage

        return salary

    else:

        raise Exception ("Employee is not found")









create_employee(1,"Chandrika",23444)

create_employee(2,"Valli",2478900)

update_employee(1,"Rasagna",56789)

#update_employee(5,"vaishnavi",56789)

delete_employee(2)

print(emp_salary(1))

show_employees()
