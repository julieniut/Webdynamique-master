from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LivreForm, NomForm
from . import models

def index(request):
    liste = list(models.Livre.objects.all())
    return render(request,'myfirstapp/index.html',{"liste": liste})


def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
     form = LivreForm(request)
     if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"myfirstapp/affiche.html",{"livre" : livre}) #envoie vers une page d'affichage du livre créé
     else:
            return HttpResponseRedirect("/myfirstapp")
    else:
        form = LivreForm() # création d'un formulaire vide
        return render(request,"myfirstapp/ajout.html",{"form" : form})


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"myfirstapp/affiche.html",{"livre" : livre})
    else:
        return render(request,"myfirstapp/ajout.html",{"form": lform})


def passion(request):
     if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = NomForm(request)
        if form.is_valid(): # validation du formulaire.
            nom = form.save() # sauvegarde dans la base
            return render(request,"myfirstapp/affiche.html",{"nom" : nom}) #envoie vers une page d'affichage du livre créé
        else:
            return HttpResponseRedirect("/myfirstapp/")
     else:
         form = NomForm() # création d'un formulaire vide
         return render(request,"myfirstapp/passion.html",{"form" : form})

def traitementnom(request):
    nform = NomForm(request.POST)
    if nform.is_valid():
        nom = nform.save()
        return render(request,"myfirstapp/affiche.html",{"nom" : nom})
    else:
        return render(request,"myfirstapp/passion.html",{"form": nform})



def updatelivre(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
            livre = lform.save(commit=False)
            livre.id = id # modification de l'id de l'objet
            livre.save() # mise à jour dans la base puisque l'id du livre existe déja.
            return HttpResponseRedirect("/myfirstapp/")
    else:
            return render(request, "myfirstapp/update.html", {"form": lform, "id": id})


def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    form = LivreForm(livre.dico())
    return render(request,"myfirstapp/ajout.html", {"form": form, "id": id})



def delete(request,id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/myfirstapp/index")


def affiche(request, id):
    livre = models.Livre.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"myfirstapp/affiche.html/", {"livre": livre})



