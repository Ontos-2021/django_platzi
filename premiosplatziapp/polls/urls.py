from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # Ejemplo: /polls/
    path("", views.IndexView.as_view(), name='index'),
    # Ejemplo: /polls/5
    path("<int:pk>/detail", views.DetailView.as_view(), name='detail'),
    # Ejemplo: /polls/5/results
    path("<int:pk>/results", views.ResultView.as_view(), name='results'),
    # Ejemplo: /polls/5/vote
    path("<int:question_id>/vote", views.vote, name='vote')
]
