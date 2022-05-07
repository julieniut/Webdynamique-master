from django.shortcuts import render

def index(request):
    return render(request, 'myfirstapp/index.html')

def passion(request):
    return render(request,'myfirstapp/passion.html',) # passe cette valeur àla vue au travers du dictionnaire de contexte