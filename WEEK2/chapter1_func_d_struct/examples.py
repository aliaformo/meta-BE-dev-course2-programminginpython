# find an employee by their employee ID

employee_list = [{"id": 12, "name": "John", "dep": "MK"}, {"id": 15, "name": "Kim", "dep": "COM"}]

def get_employee(id):
    for employee in employee_list:
        if employee['id'] == id:
            return employee
        
print("Employee from loop", get_employee(15))


# The challenge comes when the list gets bigger. 
# The code will have to iterate over the list sequentially until the number is matched. 
# Dictionary data structures

employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id]

print("Employee from dict", get_employee_from_dict(12345))

