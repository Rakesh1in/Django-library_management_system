from django import forms
from .models import Student, Book, LibraryTransaction


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_class', 'photo', 'video']



class LibraryTransactionForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = LibraryTransaction
        fields = ['student', 'book', 'start_date', 'end_date']


class BookForm(forms.ModelForm):
    year = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Book
        fields = ['name', 'author', 'publication', 'year']
