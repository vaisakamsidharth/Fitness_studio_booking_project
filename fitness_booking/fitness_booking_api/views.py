from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FitnessClass, Booking
from .serializers import BookingSerializer, FitnessClassSerializer

class ClassListView(APIView):
    # retrieve all available class lists
    def get(self, request):
        #fetch all fitness class records
        class_record = FitnessClass.objects.all()
        # used to serialize list of class object to into json format
        serializer = FitnessClassSerializer(class_record, many=True)
        return Response(serializer.data)
    
class BookingView(APIView):
    # user to book classes
    def post(self, request):
        data = request.data
        try:
            # get FitnessClass object
            fitness_class_obj = FitnessClass.objects.get(id=data['class_id'])
            # check available slots in class
            if fitness_class_obj.available_slots > 0:
                #creation of booking list
                Booking.objects.create(
                    fitness_class=fitness_class_obj,
                    client_name=data['client_name'],
                    client_email=data['client_email']
                )
                #after creation decrease the slot
                fitness_class_obj.available_slots -= 1
                fitness_class_obj.save()
                return Response({"message": "Booking successful"})
            else:
                #if slots are 0 
                return Response({"error": "No available slots"}, status=400)
        except FitnessClass.DoesNotExist:
            return Response({"error": "Class not found"}, status=404)

class BookingListView(APIView):
    # list all bookings
    def get(self, request):
        email = request.query_params.get("email")
        #validation for email didnt get
        if not email:
            return Response({"error": "Email is required"}, status=400)
        booking_record = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(booking_record, many=True)
        return Response(serializer.data)