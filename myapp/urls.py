from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_list",views.new_list, name="new_list"),
    path("single_view/<str:name>",views.single_view,name="single_view"),
    path("delete/<str:name>",views.delete,name="delete"),
    path("tasky/<str:name>",views.tasky,name="tasky"),
    path("taskn/<str:name>",views.taskn,name="taskn")
]
