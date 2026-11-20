from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:student_id>/", views.student_detail, name="student_detail"),
    path("name/<str:student_name>/", views.student_name, name="student_name"),
    path("age/", views.student_age, name="student_age"),
    path("info/", views.student_info, name="student_info"),
    path("created/", views.student_created, name="student_created"),
    path("not-found/", views.student_not_found, name="student_not_found"),
    path("compare/", views.compare_students, name="compare_students")
]