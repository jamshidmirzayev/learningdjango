from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:student_id>/", views.student_detail, name="student_detail"),
    path("name/<str:student_name>/", views.student_name, name="student_name"),
    path("age/", views.student_age, name="student_age")
]