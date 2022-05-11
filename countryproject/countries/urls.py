from django.urls import path
from countries import views
urlpatterns=[
    path('home',views.Home.as_view())
]