from django.db import models
from django.db.models import CheckConstraint, F

# Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField(null=True, blank=True, unique=True)
#     is_active = models.BooleanField(default=False)

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

# --- QuerySet LAZY ---

# students = Student.objects.all()

# students = students.filter(age__gte=18)

# students = students.filter(is_active=True)

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     discount_price = models.IntegerField()    

# --- Q() ---

# Student.objects.filter(age__gte=18, is_active=True)

# Student.objects.filter(
#     Q(age=18) | Q(age=23)
# )

# Student.objects.filter(
#     Q(age=18) & Q(is_active=True)
# )

# Student.objects.filter(
#     ~Q(age=18)
# )

# Student.objects.filter(
#     Q(age=18) ^ Q(is_active=True)
# )

# --- PK ---

# Student.object.get(id=1)
# Student.object.get(id__exact=1)
# Student.object.get(pk=1)

# --- Copying model object ---

# student = Student.objects.filter(pk=1)

# student.pk = None

# student._state.adding = True

# student.save()

# class Course(models.Model):
#     title = models.CharField(max_length=100)
    
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE,
#     )
    
# course = Course.objects.filter(pk=1)
# students = course.student_set.all()

# Reverse Relationship

# class Course(models.Model):
#     title = models.CharField(max_length=100)
    
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE,
#         related_name="python"
#     )
    
# course = Course.objects.filter(pk=1)
# students = course.student.all()

# Relationship obyektlarini boshqarish

# course = Course.objects.filter(pk=1)
# student = Student.object.filter(pk=1)

# student.course = course
# student.save()

# course = Course.objects.filter(pk=1)
# student = course.student_set.all()

# course = Course.objects.filter(pk=1)
# student = course.student_set.count()

# ManyToMany Relationships

# class Course(models.Model):
#     title = models.CharField(max_length=100)
    
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     courses = models.ManyToManyField(Course)
    
# course = Course.object.filter(pk=1)
# student = Student.courses.add(course)

# student = Student.objects.filter(pk=1)
# student.courses.all()

# student.courses.remove(course)

# student.courses.clear()

# course1 = Course.objects.filter(pk=1)
# course2 = Course.objects.filter(pk=2)

# student.courses.set([course1, course2])

# select_related(), prefetch_related()

# students = Student.objects.prefetch_related(
#     "courses"
# )

# for student in students:
#     for course in student.courses.all():
#         print(student.name, course.title)

# Save and Use

# students = Student.objects.all()

# for student in students:
#     print(student.name)
    
# for student in students:
#     print(student.name)

# More queries

# for student in Student.objects.all():
#     print(student.name)

# for student in Student.objects.all():
#     print(student.name)

# Asynchronous ORM Queries

# student = await Student.objects.filter(pk=1)

# 1

# Student.objects.filter(
#     Q(age=18) | Q(age=23)
# )

# 2

# Student.objects.filter(
#     Q(age__gte=18),
#     ~Q(is_active=False)
# )

# or 

# Student.objects.filter(
#     Q(age__gte=18) & ~Q(is_active=False)
# )

# or 

# Student.objects.filter(
#     Q(age__gte=18) & Q(is_active=True)
# )

# 3

# Product.objects.filter(
#     discount_price__lt=F("price")
# )

# 4

# students = Student.objects.filter(course__name="Python")

# 5

# course = Course.objects.get(name="Python")
# students = course.students_set.all()

# or

# course = Course.objects.get(name="Python")
# students = course.students.all()

# 6

# students = Student.objects.select_related("course")

# for student in students:
#     print(student.name, student.course.name)

# 7

# students = Student.objects.prefetch_related("courses")

# for student in students:
#     for courses in student.courses.all():
#         print(student.name, courses.name)

# 8

# student = Student.objects.get(pk=1)

# student.pk = None
# student._state.adding = True
# student.email = "new@gmail.com"
# student.save()

# 9

# Product.objects.filter(data__brand="Samsung")