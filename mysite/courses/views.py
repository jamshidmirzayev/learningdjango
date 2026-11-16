from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime

# Create your views here.

def courses_page(request):
    return HttpResponse("Courses Page!")

def python_page(request, course):
    
    course = course.capitalize()
    
    return HttpResponse(f"Courses: {course}")

def lesson_page(request, course, lesson_id):
    
    course = course.capitalize()
    
    return HttpResponse(f"Course: {course}, ID: {lesson_id}")

def lesson_time(request):
    
    now = datetime.datetime.now()
    vaqt = now.strftime("%d.%m.%Y %H:%M:%S")
    
    html = f"<h1>Current time: {vaqt}</h1>"
    
    return HttpResponse(html)