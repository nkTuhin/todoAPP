from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.HomeView.as_view(), name="home"),
# ]

urlpatterns = [
    path('', views.index, name="index"),
    # add todo urlpatterns
    path('addtodo', views.addTodo, name='addtodo'),


    # make todo undone urlpatterns
    path('un_completed_todo/<todo_ID>', views.makeUnCompleteTodo,
         name='un_completed_todo'),


    # make todo done urlpatterns
    path('completed_todo/<todoId>', views.makeCompleteTodo,
         name='completed_todo'),


    # delete completed urlpatterns
    path('delete_completed_todo', views.deleteCompletedTodo,
         name='delete_completed_todo'),

    # delete all todo urlpatterns
    path('delete_all_todo', views.deleteAll, name='delete_all_todo'),
]
