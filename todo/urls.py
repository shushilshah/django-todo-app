from django.urls import path, include
from todo import views

urlpatterns = [
    path("add_task/", views.add_task, name="add_task"),
    path("mark_as_complete/<int:pk>/",
         views.mark_as_complete, name="mark_as_complete"),
    path("mark_as_undone/<int:pk>/", views.mark_as_undone, name="mark_as_undone"),
    path("mark_as_delete/<int:pk>/", views.mark_as_delete, name="mark_as_delete"),
]
