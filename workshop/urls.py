from . import views
from django.urls import path

urlpatterns = [
    path('', views.WorkshopList.as_view(), name='workshops'),
    path('workshop/<int:id>/', views.workshop_detail, name='workshop_detail'),
    path('booking/', views.booking_display, name='bookings'),
]
