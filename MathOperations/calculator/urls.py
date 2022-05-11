from django.urls import path
from calculator import views
urlpatterns=[
    path('add',views.Addview.as_view(),name='addition'),
    path('sub',views.Subtratcview.as_view(),name='subtraction'),
    path('square',views.Square.as_view(),name='square'),
    path('cube',views.Cube.as_view(),name='cube'),
    path('fact',views.Factorial.as_view(),name='factorial'),
    path('prime',views.PrimeView.as_view(),name='primenumbers'),
    path('wordcount',views.WordCount.as_view(),name='wordcount'),
    path('home',views.IndexView.as_view(),name='home'),
]