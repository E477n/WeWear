from django.urls import path
from . import views

app_name = 'Match'
urlpatterns = [
    # /Match/
    path('match/', views.match, name='match'),
    path('matching/', views.matching, name='matching'),
]