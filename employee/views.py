from django.shortcuts import render,redirect
from .models import Employee,Attendance
from .forms import EmployeeForm
from datetime import date
# Create your views here.
def employee_list(request):
    employees=Employee.objects.all()
    return render(request,'employee_list.html',{'employees':employees})

def add_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form=EmployeeForm()
    return render(request,'add_employee.html',{'form':form})

def edit_employee(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form=EmployeeForm(instance=employee)
    return render(request,'edit_employee.html',{'form':form})

def delete_employee(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':

        employee.delete()
        return redirect('employee_list')
    return render(request,'delete_employee.html',{'employee':employee})

def dashboard(request):

    total_employees = Employee.objects.count()

    today = date.today()

    present_count = Attendance.objects.filter(
        date=today,
        status='Present'
    ).count()

    absent_count = Attendance.objects.filter(
        date=today,
        status='Absent'
    ).count()

    department_count = Employee.objects.values(
        'department'
    ).distinct().count()

    return render(
        request,
        'dashboard.html',
        {
            'total_employees': total_employees,
            'present_count': present_count,
            'absent_count': absent_count,
            'department_count': department_count,
        }
    )

def attendance(request):

    employees = Employee.objects.all()

    today = date.today()

    if request.method == 'POST':

        for employee in employees:

            status = request.POST.get(
                f'status_{employee.id}'
            )

            if status:

                Attendance.objects.update_or_create(
                    employee=employee,
                    date=today,
                    defaults={
                        'status': status
                    }
                )

        return redirect('attendance')

    return render(
        request,
        'attendance.html',
        {
            'employees': employees,
            'today': today
        }
    )

def attendance_history(request):

    attendance_records = Attendance.objects.select_related(
        'employee'
    ).order_by('-date')

    return render(
        request,
        'attendance_history.html',
        {
            'attendance_records': attendance_records
        }
    )
   