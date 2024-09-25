# serializers.py
from rest_framework import serializers
from .models import Student, Book,LibraryTransaction

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'student_class', 'photo', 'video']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'publication', 'year']

class LibraryTransactionSerializer(serializers.ModelSerializer):
    # student = StudentSerializer()  
    # book = BookSerializer()     

    class Meta:
        model = LibraryTransaction
        fields = ['id', 'student', 'book', 'start_date', 'end_date']
