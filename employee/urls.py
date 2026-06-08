from django.urls import path
from .views import create_employee,update_employee,employee_list,delete_employee,create_department,update_department,delete_department

urlpatterns=[
    path('', employee_list, name="list"),
    path('create/',create_employee, name="create"),
    path('update/<int:pk>/',update_employee,name="update"),
    path('delete/<int:pk>/',delete_employee, name="delete"),
    path('createD/',create_department, name="createD"),
    path('updateD/<int:pk>/',update_department,name="updateD"),
    path('deleteD/<int:pk>/',delete_department, name="deleteD"),
]