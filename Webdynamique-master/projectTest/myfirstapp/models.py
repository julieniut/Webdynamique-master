from django.db import models

class Livre(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    titre = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    auteur = models.CharField(max_length=100,null=True, blank=True)
    date_parution = models.DateField(blank=True, null=True) # champs de type date,pouvant être null ou ne pas être rempli
    nombre_pages = models.IntegerField(blank=False) # champs de type entier devant être obligatoirement rempli
    resume = models.TextField(max_length=1500, null=True, blank=True) # champs de type text long
    imaurl = models.URLField(max_length=300, null=True, blank=True)
    nom = models.ForeignKey("nom", on_delete=models.CASCADE,null=True)
    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur} édité le {self.date_parution}"
        return chaine

    def dico(self):
        return {"titre":self.titre,'auteur':self.auteur,'date_parution':self.date_parution,'nombres_pages':self.nombre_pages,'resume':self.resume,'imaurl':self.imaurl,"nom":self.nom}



class Nom(models.Model):
    Nom = models.CharField(max_length=15)

    def __str__(self):
        chaine = f" Votr nom: {self.Nom} "
        return chaine

    def dico(self):
        return {"Nom": self.Nom,}
