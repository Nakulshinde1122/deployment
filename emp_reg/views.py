from django.shortcuts import render
from datetime import datetime
from emp_reg.models import Employee
# Create your views here.


def welcome_page(request):
    return render(request, template_name='employee.html')


def save_update_employee(request):
    error_message = ""
    success_message = ""
    if request.method == 'POST':
        formdata = request.POST
        print("FORMDATA", formdata)
        eid = formdata.get('eid')
        ename = formdata.get('ename')
        if not ename:
            error_message = "Employee Name cannot be Empty"
        else:
            eage = formdata.get('eage')
            erole = formdata.get('erole')
            email = formdata.get('eemail')
            edj = formdata.get('edate')
            eaddr = formdata.get('eaddress')
            ephone = formdata.get('ephone')
            # currentdate = datetime.now()
            parts = edj.split('/')
            edj = datetime(int(parts[2]), int(parts[1]), int(parts[0]))

            emp = Employee(name=ename, age=eage, email=email, role=erole, phone_number=ephone, address=eaddr,
                     joining_date=edj)
            emp.save()
            success_message = "Employee Record Saved..!"
        return render(request, 'employee.html', {"success_message": success_message, "error_message": error_message})




def edit_employee(request):
    pass


def delete_employee(request):
    pass

