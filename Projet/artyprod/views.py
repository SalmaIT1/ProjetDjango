from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import  ProjetForm , ContactForm ,ReviewForm,  RegistrationForm , LoginForm
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse_lazy
from .models import Projet, Service , Equipe , Contact , Personnel , Detail , Review
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import io
from django.utils.html import strip_tags
import csv



def home(request):
    reviews = Review.objects.all()
    return render(request, 'artyprod/home.html', {'reviews': reviews})

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')




@login_required
def project_request(request):
    services = Service.objects.all()
    if request.method == 'POST':
        projetForm = ProjetForm(request.POST)
        if projetForm.is_valid():
            project = projetForm.save(commit=False)
            project.user = request.user  # Set the user to the currently authenticated user
            project.save()

            selected_services = request.POST.getlist('services')
            for service_id in selected_services:
                service = Service.objects.get(pk=service_id)
                project.services.add(service)
            
            return redirect('home')
    else:
        projetForm = ProjetForm(initial={'user': request.user.username})
    
    return render(request, 'artyprod/project_request.html', {'projetForm': projetForm, 'services': services})


def completed_projects(request):
    completed_projects = Projet.objects.filter(acheve=True)
    context = {'completed_projects': completed_projects}
    return render(request, 'your_template.html', context)

 
def project_details(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    
    context = {
        'projet': projet,
        'pk': pk,  # Add 'pk' to the context
    }
    
    return render(request, 'project_details.html', context)


def my_projects(request):
    current_user = request.user
    ongoing_projects = Projet.objects.filter(user=current_user, acheve=False)
    completed_projects = Projet.objects.filter(user=current_user, acheve=True)

    context = {
        'ongoing_projects': ongoing_projects,
        'completed_projects': completed_projects,
    }

    return render(request, 'my_projects.html', context)








def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            
            message = form.cleaned_data['message']

            # create a new Contact object with the form data
            contact = Contact(nom=nom, prenom=prenom, email=email, tel=phone,message=message)
            contact.save()

            messages.success(request, 'Votre message a été envoyé avec succès!')
            return HttpResponseRedirect('contact')

    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'artyprod/contact.html', context)




def personnel_view(request):
    personnel = Personnel.objects.all()
    context = {
        'personnel': personnel,
    }
    return render(request, 'equipe.html', context)    


def projet_details_csv(request, projet_id):
    projet = get_object_or_404(Projet, pk=projet_id)
    services = projet.detail_set.all().values_list('service__type', flat=True)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{projet.libellai}_details.csv"'

    # Use the io.StringIO object to write to a string buffer
    buffer = io.StringIO()
    writer = csv.writer(buffer)

    # Set bold font style
    bold_style = 'font-weight:bold'

    # Write the project details with spacing and colon separator
    
    writer.writerow(['Project Libelle', f': {projet.libellai}'])
    writer.writerow([])
    writer.writerow(['Service Type', f': {", ".join(services)}'])  # Use services as is, without quotes
    writer.writerow([])
    writer.writerow(['Description :', ''])  # Empty cell for spacing
    writer.writerow([strip_tags(projet.description)])  # Write the description in the next row
    writer.writerow([])
    writer.writerow(['Start Date', f': {projet.date_debut}'])
    writer.writerow([])
    writer.writerow(['End Date', f': {projet.date_fin}'])

    # Get the buffer contents and encode it as UTF-8
    csv_data = buffer.getvalue().encode('utf-8')

    # Replace comma with a colon and remove extra comma
    csv_data = csv_data.replace(b',', b'').replace(b':,', b':')

    # Set the appropriate headers for CSV download
    response.write(csv_data)
    response['Content-Length'] = len(csv_data)

    # Set additional headers for formatting
    response['Content-Transfer-Encoding'] = 'binary'
    response['Cache-Control'] = 'private, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response

def portfolio_view(request):
    projet = Projet.objects.exclude(acheve=False)
    context = {
        'projet': projet
    }
    return render(request, 'portfolio.html', context)

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    reviews = Review.objects.all()
    return render(request, 'submit_review.html', {'form': form})

def display_reviews(request):
    reviews = Review.objects.all()
    print(reviews)
    return render(request, 'home.html', {'reviews': reviews})

