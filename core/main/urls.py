from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:id>/', views.prods, name='prods'),
    path('detail/<int:id>/', views.prods_detail, name='prods_detail'),
]