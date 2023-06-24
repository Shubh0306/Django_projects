
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('resume/', views.profileView.as_view(), name='resume'),
    path('ist/', views.profileView.as_view(), name='list'),
] 