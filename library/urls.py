from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('borrowed/', views.borrowed_books, name='borrowed_books'),


]
