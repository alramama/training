from student import views
#from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('create_stud', views.create_stud),
    path('', views.show_stud),
    path('show_stud', views.show_stud),
    path('update_stud/<str:id>', views.update_stud),
    path('delete_stud/<str:id>', views.delete_stud),
    path("index1", views.index1, name="index1")

]
