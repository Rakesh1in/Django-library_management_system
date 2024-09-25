from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, BookViewSet,LibraryTransactionViewSet



router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'books', BookViewSet)
router.register(r'library-transactions', LibraryTransactionViewSet)

urlpatterns = [
    #for api default and for home
    path('', include(router.urls)),
    path('home/', views.homepage, name='homepage'),
    #students urls
    path('studentshtml/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('student_edit/<int:pk>/',views.student_edit,name='student_edit'),
    path('student_delete/<int:pk>/',views.student_delete,name='student_delete'),
    # Book URLs
    path('bookshtml/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),
    # Library Transaction URLs
    path('transactionshtml/', views.librarytransaction_list, name='librarytransaction_list'),
    path('transactions/create/', views.librarytransaction_create, name='librarytransaction_create'),
    path('transactions/edit/<int:pk>/', views.librarytransaction_edit, name='librarytransaction_edit'),
    path('transactions/delete/<int:pk>/', views.librarytransaction_delete, name='librarytransaction_delete'),
    
]






