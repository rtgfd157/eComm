from django.urls import path,include
from .views import URLShortenerListView 
from .views import URLShortenerCreateView,URLShortenerDeleteView
from . import views


urlpatterns = [
path('', URLShortenerListView.as_view() , name='URLShortener-home'),

path('URLShortener/add/', URLShortenerCreateView.as_view(),name='URLShortener-add'),
path('URLShortener/delete/<int:pk>/', URLShortenerDeleteView.as_view(), name='URLShortener-del'),
path('URLShortener/update2/<int:pk>/',  views.urlshortener_updateview, name='URLShortener-up'),

]
