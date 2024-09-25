
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

class Student(models.Model):
    name = models.CharField(max_length=100,unique=True)
    student_class = models.CharField(max_length=50,unique=True)
    photo = models.ImageField(upload_to='photos/')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return self.name

class LibraryTransaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.book.name}"

