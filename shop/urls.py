from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="Index Shop"),
    path('about/',views.about,name="About"),
    path('contact/',views.contact,name="ContactUS"),
    path('products/<int:myid>',views.productView,name="ProductView"),
    path('search',views.search,name="Search"),
    path('checkout',views.checkout,name="Checkout"),
    path('tracker/',views.tracker,name="Tracker"),
]
