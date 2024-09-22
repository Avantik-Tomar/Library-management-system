from django.shortcuts import render, redirect
from .models import Book, Student, Borrow  # Ensure Borrow is imported
from .forms import BookForm, StudentForm

def home(request):
    print("Home view called")
    return render(request, 'library/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'library/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'library/add_student.html', {'form': form})

def borrow_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        student_id = request.POST.get('student_id')
        book = Book.objects.get(id=book_id)
        student = Student.objects.get(id=student_id)
        Borrow.objects.create(book=book, student=student)
        return redirect('book_list')
    books = Book.objects.filter(available_copies__gt=0)
    students = Student.objects.all()
    return render(request, 'library/borrow_book.html', {'books': books, 'students': students})

def borrowed_books(request):
    borrowed = Borrow.objects.select_related('book', 'student').all()
    return render(request, 'library/borrowed_books.html', {'borrowed': borrowed})
