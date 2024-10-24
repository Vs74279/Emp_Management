from django.shortcuts import render,  redirect,HttpResponse,get_object_or_404
from .forms import EmpForm
from myapp.models import Emp
from django.views.decorators.csrf import csrf_exempt

def home(request):

   
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success URL
    else:
        form = EmpForm()
    return render(request, 'add_employee.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')

def view_employees(request):
    employees = Emp.objects.all()  # Get all employees from the database
    return render(request, 'view_employees.html', {'employees': employees})


@csrf_exempt
def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here, you can add the email to your mailing list or database
        return HttpResponse("Thank you for subscribing!")
    return HttpResponse("Invalid request.")

def follow_view(request):
    return render(request, 'follow.html')

def delete_employee(request, id):
    employee = get_object_or_404(Emp, id=id)  # Get the employee object
    if request.method == 'POST':
        employee.delete()  # Delete the employee
        return redirect('view_employees')  # Redirect to the employee view page
    return render(request, 'confirm_delete.html', {'employee': employee})

