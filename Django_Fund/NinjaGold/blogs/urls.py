from django.urls import path
from . import views

urlpatterns = [
    path('', views.placeholder),
    path('/new', views.newBlog),
    path('/create', views.create),
    path('/<int:number>', views.show),
    path('/<int:number>/edit', views.edit),
    path('/<int:number>/destroy', views.destroy),
]