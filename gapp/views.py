

from django.shortcuts import render, get_object_or_404, redirect

from gapp.forms import BookForm, StudentForm,LibraryTransactionForm

from .models import Student,Book,LibraryTransaction

from rest_framework import viewsets

from .models import Student, Book

from .serializers import StudentSerializer, BookSerializer,LibraryTransactionSerializer
def homepage(request):
    pass
    return render(request,'base.html')


# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Create a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# Edit an existing student
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

# Delete a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

# List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Create a new book
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

# Edit an existing book
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form})


# Delete a book
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

# List all library transactions
def librarytransaction_list(request):
    transactions = LibraryTransaction.objects.all()
    return render(request, 'librarytransaction_list.html', {'transactions': transactions})

# Create a new library transaction
def librarytransaction_create(request):
    if request.method == 'POST':
        form = LibraryTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('librarytransaction_list')
    else:
        form = LibraryTransactionForm()
    return render(request, 'librarytransaction_form.html', {'form': form})

# Edit an existing library transaction
def librarytransaction_edit(request, pk):
    transaction = get_object_or_404(LibraryTransaction, pk=pk)
    if request.method == 'POST':
        form = LibraryTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('librarytransaction_list')
    else:
        form = LibraryTransactionForm(instance=transaction)
    return render(request, 'librarytransaction_form.html', {'form': form})

# Delete a library transaction
def librarytransaction_delete(request, pk):
    transaction = get_object_or_404(LibraryTransaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('librarytransaction_list')
    return render(request, 'librarytransaction_confirm_delete.html', {'transaction': transaction})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LibraryTransactionViewSet(viewsets.ModelViewSet):
    queryset = LibraryTransaction.objects.all()
    serializer_class = LibraryTransactionSerializer



