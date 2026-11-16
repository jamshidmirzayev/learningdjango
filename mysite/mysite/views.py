from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime

def my_custom_page_not_found_view(request, exception):
    return render(request, "404.html", status=404)