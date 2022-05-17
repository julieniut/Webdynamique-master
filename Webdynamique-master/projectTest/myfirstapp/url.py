from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("passion/", views.passion),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('traitementnom/', views.traitementnom),
    path('affichenom/<int:id>/', views.affiche),
    path('update/<int:id>/',views.update),
    path('updatelivre/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
]
