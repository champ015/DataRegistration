from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import employee
def empdata(request,id=0):
    if request.method=='GET':
        if id==0:
            form=EmployeeForm()
        else:
            emp=employee.objects.get(pk=id)
            form=EmployeeForm(instance=emp)
        return render(request,'DataRegister/Display.html',{'form':form})
    else:
        if id==0:
            form=EmployeeForm(request.POST)
        else:
            emp=employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect("/Radha/Krishna")
def empList(request):
    context={'employee_list':employee.objects.all()}
    return render(request,'DataRegister/List.html',context)
def Delete(request,id):
    emp=employee.objects.get(pk=id)
    emp.delete()
    return redirect('/Radha/Krishna')

# Create your views here.
