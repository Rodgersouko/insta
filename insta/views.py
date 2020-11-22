from django.shortcuts import render
from insta.models import instagal

def display(request):
    resultsdisplay=instagal.objects.all()
    return render(request, 'index.html', {'instagal': resultsdisplay})