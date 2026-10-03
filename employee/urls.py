from django.urls import path
from . import views

urlpatterns=[
    path('',views.employee_list,name='employee_list'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('attendance/',views.attendance,name='attendance'),
    path('attendance/',views.attendance_history,name='attendance_history'),
    path('add/',views.add_employee,name='add_employee'),
    path('edit/<int:id>/',views.edit_employee,name='edit_employee'),
    path('delete/<int:id>/',views.delete_employee,name='delete_employee'),
    
]