from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm, DepartmentForm
from django.shortcuts import redirect
from .models import Employee, Department


# Create view
def create_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm()

    return render(request, 'create.html',{'form':form})

# List view
def employee_list(request):
    employee=Employee.objects.all()
    department=Department.objects.all()
    return render(request, 'list.html',{'employees':employee, 'departments':department})

#Update view
def update_employee(request, pk):
    employee=Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('list')
    
    else:
        form=EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form':form})

# Delete view
def delete_employee(request, pk):
    employee=Employee.objects.get(id=pk)
    if request.method=='POST':
        employee.delete()
        return redirect('list')
    

# Create view Department
def create_department(request):
    if request.method=='POST':
        form=DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = DepartmentForm()

    return render(request, 'createD.html',{'form':form})


#Update view Department
def update_department(request, pk):
    department=Department.objects.get(id=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            return redirect('list')
    
    else:
        form=DepartmentForm(instance=department)
    return render(request, 'updateD.html', {'form':form})


# Delete view Department
def delete_department(request, pk):
    department=Department.objects.get(id=pk)
    if request.method=='POST':
        department.delete()
        return redirect('list')