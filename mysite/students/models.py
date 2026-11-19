from django.db import models
from django.db.models import CheckConstraint

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=False)

# Many-To-One
    
# class Course(models.Model):
#     name = models.CharField(max_length=100)
    
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE
#     )

# Many-To-Many

# class Course(models.Model):
#     name = models.CharField(max_length=100)
    
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     courses = models.ManyToManyField(Course)

# One-To-One

# class Student(models.Model):
#     name = model.CharField(max_length=100)
    
# class StudentProfile(models.Model):
#     name = models.CharField(max_length=100)
#     student = models.OneToOneField(
#         Student,
#         on_delete=models.CASCADE
#     )

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
    
#     def __str__(self):
#         return self.name

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
    
# class Meta:
#     ordering = ["name"]
#     db_table = "students"

# Student.objects.all()
# Student.objects.create(name="Jamshid", 
# 
# age=23)
# Student.objects.filter(age=23)

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(CheckConstraint(age >= 18))
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.name
    
# # --- CREATE ---

# #1-way

# student = Student(
#     name = "jamshid",
#     age = 23,
#     email = "jama@gmail.com"
# )

# students.save()
    
# #2-way

# Student.objects.create(
#     name = "jamshid",
#     age = 23,
#     email = "jama@gmail.com"
# )

# # --- READ ---

# student = Student.objects.all()

# # --- FILTER ---
# # Always returns QuerySet, if it is 1 or not found whatever
# # There is not Error, only QuerySet data, empty QuerySet or One QuerySet data

# student = Student.objects.filter(age=23)
# student = Student.objects.filter(name="jamshid")
# student = Student.objects.filter(is_active=True)
# student = Student.objects.filter(age=23, is_active=True)
# student = Student.objects.filter(name="jamshid", is_active=True)

# # --- GET ---

# student = Student.object.get(id=1)
# student = Student.object.get(name="jamshid")
# student = Student.object.get(email="jama@gmail.com")

# # --- EXCLUDE ---
# # ...dan tashqari hamma
# ## ...ni natijadan chiqarib qolgan hammasini return

# student = Student.objects.exclude(age=23)

# # --- LOOKUPS ---

# Student.objects.filter(age__gt=18)
# Student.objects.filter(age__gte=25)
# Student.objects.filter(name__icontains="jam")
# Student.objects.filter(email__endswith="gmail.com")

# # --- ORDER_BY ---

# students = Student.objects.all().order_by("age")
# students = Student.objects.all().order_by("-age")
# students = Student.objects.all().order_by("name")

# # --- LIMIT ---

# students = Student.objects.all()[:5]
# students = Student.objects.all()[:10]

# # --- UPDATE ---

# student = Student.objects.get(id=1)

# student.age = 24

# student.save()

# Student.objects.filter(id=1).update(age=24)

# Student.objects.filter(is_active=False).update(is_active=True)

# # --- DELETE ---

# student = Student.objects.get(id=1)

# student.delete()

# Student.objects.filter(id=1).delete()

# Student.objects.all().delete()

# # --- QuerySet LAZY ---

# students = Student.objects.all()

# students = students.filter(age__gte=18)

# students = students.filter(is_active=True)

