from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('about/', views.about , name = 'about'),
    path('contact/', views.contact , name = 'contact'),
    path('thanks/', views.contact_thanks , name = 'contact2'),
    path('events/', views.events , name = 'events'),
    path('events/cultural/', views.cultural_events , name = 'cultural'),
    path('events/informal/', views.informal_events , name = 'informal'),
    path('events/formal/', views.formal_events , name = 'formal'),
    path('events/literary/', views.literary_events , name = 'literary'),
    path('events/fine-arts/', views.finearts_events , name = 'fine-arts'),
]