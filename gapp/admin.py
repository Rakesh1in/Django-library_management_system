from django.contrib import admin

from django.contrib import admin
from .models import Student, Book, LibraryTransaction

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'photo', 'video')
    search_fields = ('name', 'student_class')
    list_filter = ('student_class',)
    ordering = ('name',)
admin.site.register(Student,StudentAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publication', 'year')
    search_fields = ('name', 'author')
    list_filter = ('publication', 'year')
    ordering = ('name',)
admin.site.register(Book,BookAdmin)

class LibraryTransactionAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'start_date', 'end_date')
    search_fields = ('student__name', 'book__name')
    list_filter = ('start_date', 'end_date')
    ordering = ('start_date',)
admin.site.register(LibraryTransaction,LibraryTransactionAdmin)