"""flightproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from flightapp.views import PassengerViewSet,FlightViewSet,ReservationViewSet,find_flight,save_reservation


router=DefaultRouter()
router.register('flights',FlightViewSet)
router.register('passenger',PassengerViewSet)
router.register('reservation',ReservationViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('flightservice/', include(router.urls)),
    path('flightservice/findflight',find_flight),
    path('flightservice/savereservation',save_reservation)
]