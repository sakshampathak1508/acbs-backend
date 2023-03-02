from django.urls import path
from .views import (
    ExecutivesView, MemberCountriesView, SponsersView, LatestAnnouncement, AboutUSView
)

urlpatterns = [
    path('sponsers/', SponsersView.as_view()),
    path('announcement/', LatestAnnouncement.as_view()),
    path('about-us/', AboutUSView.as_view()),
    path('executives/', ExecutivesView.as_view()),
    path('member-countries/',  MemberCountriesView.as_view())
]