from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def home(request):
    emp_form = EmployeeForm()
    return render(request, 'home.html', {'form':emp_form})


def get_employee(request):
    print("insid ete get all employee ")
    context = {}
    data = Employee.objects.all()
    print(data)
    context['employees'] = data
    return render(request, 'list_view.html', context)


def get_employee_id(request, id):
    print("####inside the get_employee_id")
    context = {}
    data = Employee.objects.filter(employee_id=id)
    print(data)
    context['employees'] = data
    return render(request, 'display_employee.html', context)


def create_employee(request):
    print("####inside the create employee")
    largest = Employee.objects.all().order_by('employee_id').last()
    curr_emp = largest.employee_id
    new_emp = curr_emp + 1
    data = EmployeeForm(request.POST)

    if data.is_valid():
        form_data = data.cleaned_data                    
        emp = Employee(employee_id = new_emp,
                        first_name = form_data['first_name'],         
                        last_name  = form_data['last_name'],
                        email_id = form_data['email_id'],
                        phone_number = form_data['phone_number'],
                        date_of_birth = form_data['date_of_birth'])
        emp.save()
    else:
        raise "Form is not valid"

    # return render(request, 'create_view.html', context)
    # return  get_employee_id(request, new_emp)
    return redirect('display_employee', id=new_emp)



def update_employee(request, id):
    exists_data = Employee.objects.get(employee_id = id)    
    if request.method == 'POST':
        form_data = EmployeeForm(request.POST, instance=exists_data)
        if form_data.is_valid():
            form_data.save()
            return redirect('display_employee', id=id)
        else:
            print(form_data.errors.as_data())            
    else:
        form_data = EmployeeForm(instance=exists_data) # in order to pass the existing data we need to remove request.POST

    return render(request, 'update_employee.html',  {'form':form_data, 'id':id})


def delete_employee(request, id)    :
    context ={}
    emp_obj = get_object_or_404(Employee, employee_id = id)
    emp_obj.delete()
    return redirect('list_employee')
