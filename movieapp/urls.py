
from django.urls import path

from movieapp import views
app_name = "movieapp"

urlpatterns = [

    path('', views.Index,name="index"),
    path('movie/<int:movie_id>/',views.detail,name="detail"),
    path('add/',views.add_movie,name="add"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/', views.delete, name="delete")


]