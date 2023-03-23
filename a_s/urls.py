from django.urls import path, include
from a_s import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_autosys, name='add_autosys'),
    path('names/', views.show_names, name='show_names'),
    path('neighbours/', views.list_neighbours, name='list_neighbours'),
    path('neighbours/<asn_id>', views.show_neighbours, name='show_neighbours'),
    path('whois/', views.whois, name='whois'),
    path('whois_list/', views.whois_list, name='whois_list'),
    path('whois_list/<asn_id>', views.show_whois, name='show_whois'),
]
