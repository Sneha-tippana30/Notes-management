from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addnote, name='addnote'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('python/', views.python, name='python'),
    path('django/', views.django, name='django'),
    path('sql/', views.sql, name='sql'),
    path('frontend/', views.frontend, name='frontend'),
    path('aiml/', views.aiml, name='aiml'),
       
]
