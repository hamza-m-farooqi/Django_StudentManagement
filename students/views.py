from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, "students/index.html",{
        'Students':Student.objects.all()
    })
def detail(request,id):
    _Student=Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
def add(request):
    if request.method=='POST':
        _StudentForm=StudentForm(request.POST)
        if _StudentForm.is_valid():
            NewStudent=Student(
                student_number=_StudentForm.cleaned_data['student_number'],
                first_name=_StudentForm.cleaned_data['first_name'],
                last_name=_StudentForm.cleaned_data['last_name'],
                email=_StudentForm.cleaned_data['email'],
                field_of_study=_StudentForm.cleaned_data['field_of_study'],
                gpa=_StudentForm.cleaned_data['gpa'],
            )
            NewStudent.save()
            return render(request, "students/add.html",{
                'Form':_StudentForm,
                'Success':True
            })
    else:
        return render(request, "students/add.html",{
                'Form':StudentForm(),
                'Success':None
            })
def edit(request,id):
    print(id)
    _Student=Student.objects.get(pk=id)
    if request.method=='POST':
        _StudentForm=StudentForm(request.POST,instance=_Student)
        if _StudentForm.is_valid():
            _StudentForm.save()
            return render(request, 'students/edit.html',{
                'Form':_StudentForm,
                'Success':True
            })
    else:
        _StudentForm=StudentForm(instance=_Student)
        return render(request, 'students/edit.html',{
            'Form':_StudentForm
        })
def delete(request,id):
    if request.method=='POST':
        _Student=Student.objects.get(pk=id)
        _Student.delete()
        return HttpResponseRedirect(reverse('index'))