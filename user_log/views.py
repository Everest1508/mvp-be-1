from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
import random
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class SignupView(APIView):
    
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        user=User(request.data)
    
        serializer = UserSerializer(data=request.data)
        
        print(request.data)
        if serializer.is_valid():
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            user = serializer.save()
            return Response({'access_token': access_token,"message":"OTP sent on mail"}, status=status.HTTP_201_CREATED)
            
            
            return Response({"data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

 
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(Q(password=password) and Q(email=email)).first()
        return Response(status=status.HTTP_200_OK, data={
            'access': str(RefreshToken.for_user(user).access_token),
            'refresh': str(RefreshToken.for_user(user)),
            'user': {
                "name":user.name,
                "email":user.email,
                "phone":user.phone,
                "age ":user.age,
                "college":user.college,
                "password":user.password,
                'email': user.email,
                'is_active': user.is_active
            }
        })
        
        
class VerifyOTPView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp_entered = request.data.get('otp')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not user.otp:
            return Response({'error': 'OTP not generated'}, status=status.HTTP_400_BAD_REQUEST)

        if otp_entered == user.otp:
            user.otp = None
            user.save()
            user.is_active = True
            user.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)        
        
class Users(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
       

        
class CollegeListCreateView(APIView):
    def get(self, request):
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GamesListCreateView(APIView):
    def get(self, request):
        games = Games.objects.all()
        serializer = GamesSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GamesListCreateView(APIView):
    def get(self, request):
        games = Games.objects.all()
        serializer = GamesSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubEventCreateAPIView(APIView):
    def get(self,request):
        events = SubEvents.objects.all()
        serializer = SubEventsSerializer(events,many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = SubEventsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddUserView(APIView):
    def post(self, request, id, *args, **kwargs):
        sub_event = get_object_or_404(SubEvents, pk=id)

        try:
            user = User.objects.get(pk=request.data['id'])
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.participation = True
        user.participated_event = sub_event.id
        user.save()
        sub_event.participants.add(user)

        return JsonResponse({"message": "Stored Successfully"})
    
class MainEventCreateAPIView(APIView):
    def get(self,request):
        events = MainEvent.objects.all()
        print(events)
        serializer = MainEventsSerializer(events,many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = SubEventsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyEventView(APIView):
    def get(self,request,id):
        user = User.objects.get(id=id)
        participated_event_id = user.participated_event
        event = SubEvents.objects.filter(id=participated_event_id)
        print(event)
        serializer = SubEventsSerializer(event,many=True)
        return Response(serializer.data)