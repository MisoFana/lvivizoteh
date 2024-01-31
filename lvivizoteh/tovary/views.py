from django.shortcuts import render
from .models import Staff


def index(request):
    staff = Staff.objects.all()
    return render(request, 'index.html', {'staff': staff})
