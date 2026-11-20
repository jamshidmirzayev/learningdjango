from django.shortcuts import render
from django.http import HttpResponse, Http404
from students.models import Student

# Create your views here.

def index(request):
    return HttpResponse("Students List")

def student_detail(request, student_id):
    return HttpResponse(f"Student ID: {student_id}")

def student_name(request, student_name):
    
    data = ["Jamshid"]
    kichik = [name.lower() for name in data]
    
    if student_name.lower() in kichik:
        student_name = student_name.capitalize()
        return HttpResponse(f"Student name: {student_name}", content_type="text/plain")
    else:
        raise Http404("Name is not in Data!")
    
def student_age(request):
    age = request.GET.get("age")
    return HttpResponse(f"Age: {age}")

def student_info(request):
    return HttpResponse("Student Information")

def student_created(request):
    return HttpResponse("Student created", status=201)

def student_not_found(request):
    raise Http404("Student not found")

def compare_students(request):
    id1 = request.GET.get("id1")
    id2 = request.GET.get("id2")

    student1 = Student.objects.get(pk=id1)
    student2 = Student.objects.get(pk=id2)

    result = student1 == student2

    return HttpResponse(result)

# Asynchronous ORM Queries

# async def student_info(request):
#     student = await Student.object.aget(pk=1)
#     return HttpResponse(student.name)

