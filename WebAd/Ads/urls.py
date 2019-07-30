from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('adServiceRedirect',views.adServiceRedirect,name="Redirect2Ad"),
    path('fetchTextAd',views.fetchTextAd,name="FetchTextAd"),
    path('logIn',views.logIn,name="logIn"),
    path('signUp',views.signUp,name="signUp"),
    path('logOut',views.logOut,name="logOut"),
    path('webMonetize/',include('Ads.webMonetize_urls')),
    path('adProvider/',include('Ads.adProvider_urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
