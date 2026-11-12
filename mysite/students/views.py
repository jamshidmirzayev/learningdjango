from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Students App!")

def student_detail(request, student_id):
    return HttpResponse(f"Student ID: {student_id}")

def student_name(request, student_name):
    
    data = ["Jamshid"]
    kichik = [name.lower() for name in data]
    
    if student_name.lower() in kichik:
        student_name = student_name.capitalize()
        return HttpResponse(f"Student name: {student_name}", content_type="text/plain")
    else:
        return HttpResponse("Name is not in Data!", status=404, content_type="text/plain")
    
def student_age(request):
    age = request.GET.get("age")
    return HttpResponse(f"Age: {age}")