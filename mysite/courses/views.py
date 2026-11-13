from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses_page(request):
    return HttpResponse("Courses Page!")

def python_page(request, course):
    
    course = course.capitalize()
    
    return HttpResponse(f"Courses: {course}")

def lesson_page(request, course, lesson_id):
    
    course = course.capitalize()
    
    return HttpResponse(f"Course: {course}, ID: {lesson_id}")