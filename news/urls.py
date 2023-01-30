from django.urls import path
from .views import (
    AllNewsApiView,YearNewsView,NewsView,
)
# LatestNewsView,FeaturedNewsView
urlpatterns = [
    path('', NewsView.as_view(),name="one news"),
    path('all/', AllNewsApiView.as_view(),name="all news"),
    path('year/', YearNewsView.as_view(),name="Year wise news"),
    # path('latest/', LatestNewsView.as_view(),name="Latest"),
    # path('featured/', FeaturedNewsView.as_view(),name="Featured"),
]