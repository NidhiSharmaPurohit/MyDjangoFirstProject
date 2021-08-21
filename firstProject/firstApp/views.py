from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
# Create your views here.

def employeeView(request):
    emp = {
    'id' : 123,
    'name' : 'nidhi',
    'sal' : 1000000,
    }

    data=Employee.objects.all()
    response={'Employee' : list(data.values('name','sal'))}

    response1={'Employee' : list(data)}

    return JsonResponse(response)





def salaryView(request):
    sal=[
    {
    'name': 'ashutosh',
    'salary' : 10
    },
    {
    'name': 'nidhi',
    'salary' : 1000
    },
    {
    'name': 'pranav',
    'salary' : 1004
    },
    ]

    return JsonResponse(sal,safe=False)
