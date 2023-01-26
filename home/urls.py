from django.urls import path
from .views import SponsersView, LatestAnnouncement, AboutUSView
urlpatterns = [
    path('sponsers/', SponsersView.as_view()),
    path('announcement/', LatestAnnouncement.as_view()),
    path('about-us/', AboutUSView.as_view())
]