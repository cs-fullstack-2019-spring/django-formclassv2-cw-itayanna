

# importing info from forms page and render function


from django.shortcuts import render
from .forms import jobApp

# Create your views here.


# function for the browser set ups

def index(request):
    if(request.method == 'POST'):
        print(request.POST["name"])
        name = request.POST["name"]
        dob= request.POST['dateOfBirth']
        position = request.POST['positionApplyingTo']
        salary = request.POST['salary']
        context = {"name": name, 'dateOfBirth': dob,
                   'position': position, 'salary': salary

                   }
        return render(request, "employeeApp/appInfo.html", context)

    else:
        appForm = jobApp
        context = {
            'appForm' : appForm
        }
        return render(request, 'employeeApp/index.html', context)

