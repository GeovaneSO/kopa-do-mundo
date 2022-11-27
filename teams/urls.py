from django.urls import path
# from teams.views import TeamsView, Tea,
from teams import views

urlpatterns = [
    path('teams/', views.TeamsView.as_view()),
    path('teams/<int:id>/', views.TeamsDetailView.as_view()),

]