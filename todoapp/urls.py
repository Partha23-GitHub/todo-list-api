from django.urls import path
from . import views
urlpatterns = [
    path('view/',views.ToDoView.as_view(),name='todoview'),
    path('view/<int:pk>',views.ToDodescView.as_view(),name='tododescview'), #for individual todo description
]
