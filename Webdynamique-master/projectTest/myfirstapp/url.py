from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.index),
    path("passion/", views.passion),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('traitementnom/', views.traitementnom),
    path('update/<int:id>/',views.update),
    path('updatelivre/<int:id>/', views.updatelivre),
    path('delete/<int:id>/', views.delete),
]
