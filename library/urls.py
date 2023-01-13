from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('search/',views.search),
    path('home/',views.home),
    path('about/',views.aboutus),
    path('contact/',views.contactus),
    path('cs/',views.cs),
    path('ee/',views.ee),
    path('gallery/',views.gallery),
    path('ma/',views.ma),
    path('mp/',views.mp),
    path('magazines/',views.mag),

    path('csnotes/',views.csnotes),
    path('mpnotes/',views.mpnotes),
    path('eenotes/',views.eenotes),
    path('manotes/',views.manotes),

    path('cspaper/',views.cspaper),
    path('mppaper/',views.mppaper),
    path('eepaper/',views.eepaper),
    path('mapaper/',views.mapaper),
]
