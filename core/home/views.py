from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
@api_view(['GET'])
def index(request):
    data = Student.objects.all()
    serializers = StudenSerializer(data,many= True)
    return Response({'playload':serializers.data})


class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post (self,request ):
        serializer = UserSerializer(data = request.data)
        # print(request.data)
        if serializer.is_valid():
            u = serializer.save()
            u.set_password(request.data['password'])
            u.save()
            user = User.objects.get(username = serializer.data['username'])

            # token_obj , created   = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user=user)
            return Response({
                'status': 200, 
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': serializer.data})
        else:
            return Response({'status': 400, 'message': serializer.errors})


class StudentApis(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self, request):

        data = Student.objects.all()
        serializers = StudenSerializer(data,many= True)
        return Response({'playload':serializers.data})

    def post (self, request):

        serializer = StudenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Student created successfully'})
        else:
            return Response({'status': 400, 'message': serializer.errors})
    
    

    def put(self, request):
        try:

            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudenSerializer(student_obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'message': 'Student Updated successfully'})
            else:
                return Response({'status': 400, 'message': serializer.errors})
        
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': "invalid input "})

    def patch(self, request):
        try:

            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudenSerializer(student_obj,data=request.data,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'message': 'Student Updated successfully'})
            else:
                return Response({'status': 400, 'message': serializer.errors})
        
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': "invalid input "})
    def delete(self, request):
        try:

            id = request.GET.get('id')
            student_obj = Student.objects.get(id = id)
            
            student_obj.delete()
            return Response({'status': 200, 'message': 'Student Deleted successfully'})
            
        
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': e})