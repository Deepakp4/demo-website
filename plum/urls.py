from django.urls import path 
from plum import views
urlpatterns=[
    path('',views.index),
    path('home/',views.home),
    path('index/',views.index,name="index"),
    path('form/',views.form),
    path('logout/',views.logout,name="logout"),
    path('elements/',views.elements),
    path('login/',views.login,name="login"),
    path('taps/',views.taps,name="taps"),
    path('shower/',views.shower,name="shower"),
    path('pipes/',views.pipes,name="pipes"),
    path('cart/',views.cart,name="cart"),
    
    
    
]