from django.urls import path
from .views import TeamView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamView.as_view())
]