from django.shortcuts import render
from django.http import HttpResponse, Http404

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