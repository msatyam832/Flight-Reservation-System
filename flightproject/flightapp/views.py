from flightapp.models import Flight,Passenger,Reservation
from flightapp.serializer import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import  viewsets
from rest_framework import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
@api_view(['POST'])
def find_flight(request):
    flight=Flight.objects.filter(departurecity=request.data['departurecity'],arrivalcity=request.data['arrivalcity'])
    serializer=FlightSerializer(flight,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['flightId'])
    passenger=Passenger()
    passenger.firstname=request.data['firstname'],
    passenger.middlename=request.data['middlename'],
    passenger.mobileNo=request.data['mobileNo'],
    passenger.email=request.data['email']
    passenger.save()

    reservation=Reservation()
    reservation.flight=flight
    reservation.passenger=passenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)

   

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class =PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer





