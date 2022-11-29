from django.http import HttpResponse
from django.shortcuts import render
from Proyecto.models import Libro
# Create your views here.

def home(request):

    return render(request, "Proyecto/home.html")

def is1(request):
    libros= Libro.objects.all()
    return render(request, "Proyecto/is1.html", {"libros":libros})

def pr(request):
    libros= Libro.objects.all()
    return render(request, "Proyecto/pr.html", {"libros":libros})

def pd(request):
    libros= Libro.objects.all()
    return render(request, "Proyecto/pd.html", {"libros":libros})

def doo(request):
    libros= Libro.objects.all()
    return render(request, "Proyecto/doo.html", {"libros":libros})

def ts(request):
    libros= Libro.objects.all()
    return render(request, "Proyecto/ts.html", {"libros":libros})

def sbd(request):
    libros= Libro.objects.all()
    return render(request, "Proyecto/sbd.html", {"libros":libros})



