from django.urls import path
from .views import (
    ExecutivesView, MemberCountriesView, SponsersView, LatestAnnouncement, AboutUSView, SearchView, FeaturedView
)

urlpatterns = [
    path('sponsers/', SponsersView.as_view()),
    path('announcement/', LatestAnnouncement.as_view()),
    path('about-us/', AboutUSView.as_view()),
    path('executives/', ExecutivesView.as_view()),
    path('member-countries/',  MemberCountriesView.as_view()),
    path('search/',  SearchView.as_view()),
    path('featured/',  FeaturedView.as_view())
]