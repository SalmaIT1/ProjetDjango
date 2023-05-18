from django.db import models
from django import forms

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    
    def __str__(self):
        return self.username

class Service(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.type


class Equipe(models.Model):
    nom = models.CharField(max_length=255, default="Not Specified")
    membres = models.ManyToManyField('Personnel', related_name='equipes')
    projet = models.ForeignKey('Projet', on_delete=models.CASCADE, related_name='equipe_projet',
                               default=None, null=True)

    def __str__(self):
        return self.nom


class Projet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    libellai = models.CharField(max_length=255, default="not specified")
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=False)
    services = models.ManyToManyField(Service, through='Detail')
    equipes_projet = models.ManyToManyField(Equipe, related_name='projets', blank=True)

    def __str__(self):
        return self.libellai

    def create_equipe(self):
        equipe = Equipe.objects.create(nom='My Equipe', projet=self)
        self.equipes.add(equipe)
        return equipe

    @classmethod
    def create_projet_with_equipe(cls, user, libellai, description, date_debut, date_fin, acheve=False):
        projet = Projet.objects.get(id=1)
        equipe = Equipe.objects.create(nom='My Equipe', projet=projet)
        personnel = Personnel.objects.get(id=1)
        equipe.membres.add(personnel)
        return projet


class Detail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.projet.libellai} - {self.service.type} - {self.description} "

    def get_project_details_csv(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{self.projet.libellai}_details.csv"'

        writer = csv.writer(response)
        writer.writerow(['Project Description', self.projet.description])
        writer.writerow([])
        writer.writerow(['Service Type', 'Description'])
        writer.writerow([self.service.type, self.description])

        return response


class Personnel(models.Model):
    nom = models.CharField(max_length=255)
    fichier_CV = models.FileField(upload_to='cvs/')
    fichier_photo = models.ImageField(upload_to='photos/')
    lien_linkedIn = models.URLField()

    def __str__(self):
        return self.nom


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

   


    def __str__(self):
        return f"{self.prenom} - {self.nom} - {self.date_envoi}"

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name 





