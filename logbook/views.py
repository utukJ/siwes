from logbook.forms import WeekUpdateForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Workweek, Student
import datetime

# Create your views here.

def index(request):
    return render(request, "logbook/index.html")


def process_student(request):
    matric = request.GET.get("matric")
    try:
        student = Student.objects.get(matric=matric)
        return redirect("{}/allwks".format(matric))
    except Student.DoesNotExist:
        return render(request, "logbook/new.html", {"matric": matric})


def new(request, matric):
    ## get all the getables -- matric, startdate
    student = Student(matric=matric)
    student.save()
    start_date = request.GET.get("startdate")
    for i in range(24):
        wk = Workweek(author=student, week_num=i+1, start_date=start_date)
        wk.save()
    return redirect("allwks", matric=matric)


def allwks(request, matric):
    student = Student.objects.get(matric=matric)
    wks = Workweek.objects.filter(author=student)
    return render(request, "logbook/allwks.html", {"wks": wks, "matric": matric})


def editwk(request, matric, wknum):
    student = Student.objects.get(matric=matric)
    wk = Workweek.objects.get(author=student, week_num=wknum)
    form = WeekUpdateForm(instance=wk)
    print(form)
    return render(request, "logbook/editwk.html", {"form": form, "wk": wk, "matric": matric})


def update(request, matric, wknum):
    student = Student.objects.get(matric=matric)
    wk = Workweek.objects.get(author=student, week_num=wknum)
    wk.d1 = request.POST["d1"]
    wk.d2 = request.POST["d2"]
    wk.d3 = request.POST["d3"]
    wk.d4 = request.POST["d4"]
    wk.d5 = request.POST["d5"]
    wk.save()
    return redirect("editwk", matric=matric, wknum=wknum)


