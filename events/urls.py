from django.urls import path

from .views import (
    EventView,AllEventView,YearEventView,EventFrontView
)

urlpatterns = [
    path('', EventView.as_view(),name="one events"),
    path('all/', AllEventView.as_view(),name="all events"),
    path('year/', YearEventView.as_view(),name="year events"),
    path('front/', EventFrontView.as_view(),name="front events"),
]