from django.urls import path
from .views import (
    ExecutivesView, MemberCountriesView, SponsersView, LatestAnnouncement, AboutUSView, SearchView, FeaturedView,
    ContactView, DownloadView, AllChampsView, ChampsView, RulesView, CategoryView
)

urlpatterns = [
    path('sponsers/', SponsersView.as_view()),
    path('announcement/', LatestAnnouncement.as_view()),
    path('about-us/', AboutUSView.as_view()),
    path('executives/', ExecutivesView.as_view()),
    path('member-countries/',  MemberCountriesView.as_view()),
    path('search/',  SearchView.as_view()),
    path('featured/',  FeaturedView.as_view()),
    path('documents/',  DownloadView.as_view()),
    path('contact/',  ContactView.as_view()),
    path('rule/',  RulesView.as_view()),
    path('allchamps/',  AllChampsView.as_view()),
    path('champ/',  ChampsView.as_view()),
    path('category-footer/',  CategoryView.as_view()),
]