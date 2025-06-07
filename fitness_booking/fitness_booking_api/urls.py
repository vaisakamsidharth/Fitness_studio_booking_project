
from django.urls import path
from .views import ClassListView, BookingView, BookingListView

urlpatterns = [
    path('class_record', ClassListView.as_view()),
    path('book', BookingView.as_view()),
    path('booking_record', BookingListView.as_view()),
]