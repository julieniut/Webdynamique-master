from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.index),
    path("passion/", views.passion),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('identification/', views.identification),
    path('traitement2/', views.traitement2),
    path('update/<int:id>/',views.update),
    path('updatelivre/<int:id>/', views.updatelivre),
]
