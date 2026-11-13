from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses_page, name="courses_page"),
    path("python/",
         views.python_page,
         {"course": "python"},
         name="python_page"),
    path("python/<int:lesson_id>/",
         views.lesson_page,
         {"course": "python"},
         name="lesson_page"),
]