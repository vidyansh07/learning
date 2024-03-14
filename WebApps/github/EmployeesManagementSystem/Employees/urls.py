from django.urls import path
from .views import employee_list

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    # Add more URL patterns for other views (e.g., add_employee, update_employee, delete_employee)
]