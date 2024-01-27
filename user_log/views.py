from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
import random
from django.shortcuts import get_object_or_404,get_list_or_404
from django.http import JsonResponse
import jwt
from django.conf import settings
from .authentication import IsJWTAuthenticated
from .permissions import IsJWTAuthenticatedPermission


from django.shortcuts import render


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
        
        
        token = jwt.encode({
                "id":user.id,
                "name":user.name,
                "email":user.email,
                "phone":user.phone,
                "age ":user.age,
                "college":user.college,
                "password":user.password,
                'email': user.email,
                'is_active': user.is_active
            }, settings.SECRET_KEY, algorithm='HS256')
        
        
        
        if not user.is_active:
            return JsonResponse({"error":"user is not verified"})
        access = token
        
        return Response(status=status.HTTP_200_OK, data={
            'access': access,
            'user': {
                "id":user.id,
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

    def post(self, request, *args, **kwargs):
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
        title = request.data['title']
        game = request.data['game']
        description = request.data['description']
        rules = request.data['rules']
        game = Games.objects.filter(Q(title=game)).first()
        
        if not game:
            game = Games.objects.create(title=request.data['game'])
            
        main_event = MainEvent.objects.filter(Q(id=request.data['main_event_id'])).first()
        try:
            sub_event = SubEvents.objects.create(
                title=title,
                game=game,
                description=description,
                rules=rules,
            )
            sub_event.save()
            main_event.sub_events.add(sub_event)
            main_event.save()
        except:
            return Response({"message":"SubEvent not created"})
        
        serializer = SubEventsSerializer(sub_event)
        

        return Response({"message":"SubEventAdded Successfully","data":serializer.data})
    
class AddUserToEventView(APIView):
    def post(self, request, id, *args, **kwargs):
        sub_event = get_object_or_404(SubEvents, pk=id)

        try:
            user = User.objects.get(pk=request.data['id'])
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        
        print(user.participated_event)
        
        user.participation = True
        user.save()
        if str(sub_event.id) in user.participated_event:
            return JsonResponse({"error": "Already participated in this event"})
        
        
        user.participated_event = user.participated_event + str(sub_event.id)+","
        user.save()
        sub_event.participants.add(user)

        return JsonResponse({"message": "Participated Successfully"})
    
class MainEventCreateAPIView(APIView):
    
    def get(self,request):
        events = MainEvent.objects.all()
        serializer = MainEventsSerializer(events,many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        
        try:
            main_event = MainEvent.objects.create(title=request.data['title'],image=request.data['image'])
            main_event.save()
            return Response({
                "title":request.data['title'],
                "sub_events":[]
                }, status=status.HTTP_201_CREATED)

        except:
            return Response({"error":"Event not created"}, status=status.HTTP_400_BAD_REQUEST)
    
class MyEventView(APIView):
    authentication_classes = [IsJWTAuthenticated]
    # permission_classes = [IsJWTAuthenticatedPermission]
    def get(self,request,id):
        user = request.user
        participated_event_id = user.participated_event.split(",")
        print(participated_event_id[:-1])
        event = get_list_or_404(SubEvents, id__in=participated_event_id[:-1])
        print(event)
        serializer = SubEventsSerializer(event,many=True)
        return Response(serializer.data)


class AddSubEventView(APIView):
    def put(self,request,id):
        mainevent = MainEvent.objects.get(id=id)
        subevent = SubEvents.objects.get(id=request.data['id'])
        mainevent.sub_events.add(subevent)
        return JsonResponse({"message": "Sub event added successfully"})