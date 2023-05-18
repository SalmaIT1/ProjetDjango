from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Projet, Service , Personnel ,Equipe ,Review 



class RegistrationForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',error_messages={'required': ''})
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.',error_messages={'required': ''})
    username = forms.CharField(max_length=30, required=True, help_text='Required.',error_messages={'required': ''})
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.',error_messages={'required': ''})
    tel= forms.CharField(max_length=15, required=True, help_text='Required.',error_messages={'required': ''})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'tel', 'username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        register = super().save(commit=False)
        register.set_password(self.cleaned_data['password1'])
        if commit:
            register.save()
        return register  


        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        
        model = User
        fields = ['username','password']







class ProjetForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all())

    class Meta:
        model = Projet
        fields = ['libellai', 'description', 'date_debut', 'date_fin','services']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['libellai'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_debut'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['date_fin'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['services'].widget.attrs.update({'class': 'form-control'})

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First name...'}))
    prenom = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last name...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}))

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message here...', 'rows': 5}))

class AssocierEquipeProjetForm(forms.ModelForm):
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all(), required=False)

    class Meta:
        model = Projet
        fields = ['equipe']

    def __init__(self, *args, **kwargs):
        equipe_id = kwargs.pop('equipe_id', None)
        super().__init__(*args, **kwargs)
        if equipe_id:
            self.fields['equipe'].initial = equipe_id

    def save(self, commit=True):
        projet = super().save(commit=False)
        if self.cleaned_data['equipe'] is not None:
            projet.equipe_id = self.cleaned_data['equipe'].id
        else:
            projet.equipe_id = None
        if commit:
            projet.save()
        return projet

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'message']


