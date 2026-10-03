from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField()
    phone=models.CharField( max_length=15)
    department=models.CharField( max_length=50)
    designation=models.CharField(max_length=30)
    address=models.CharField( max_length=50)
    Doj=models.DateField()

    def __str__(self):
        return self.name
class Attendance(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
        ],
        default='Present'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['employee', 'date'],
                name='unique_employee_date'
            )
        ]

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"