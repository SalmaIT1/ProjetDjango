from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def accueil(request):
    return render(request,'accueil.html')

@login_required
def home(request):
    context={'val':"Menu Acceuil"}
return render(request,'home.html',context)