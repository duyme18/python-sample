employee_db = {
    1000: dict(name="Duy", age=26, doj='19960313', deft=100),
    2000: dict(name="Trang", age=26, doj='19960313', deft=200),
    3000: dict(name="Nam", age=26, doj='19960313', deft=300),
    4000: dict(name="An", age=26, doj='19960313', deft=400),
    5000: dict(name="Binh", age=26, doj='19960313', deft=500),
    6000: dict(name="Long", age=26, doj='19960313', deft=600),
}

dept_db = {
    100: 'HRD',
    200: 'FINANCE',
    300: 'ACCOUNTS',
    400: 'SALES',
    500: 'ENGINEERING',
    600: 'SUPPORT'
}


def get_employee(id):
    if id in employee_db:
        return employee_db[id]
    else:
        print(id, ' not exists')
        return


def get_deft_info(dept_id):
    if dept_id in dept_db:
        return dept_db[dept_id]
    else:
        print(dept_id, ' not exists')
        return


def display_employee(employee_data):
    for key, value in employee_data.items():
        if key == 'deft':
            print(key, ' : ', get_deft_info(value))
        else:
            print(key, ' : ', value)


emp_id = int(input("Please Enter Emp Id :"))

emp_data = get_employee(emp_id)

if emp_data:
    display_employee(emp_data)
