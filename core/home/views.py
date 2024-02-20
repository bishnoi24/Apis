from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
@api_view(['GET'])
def index(request):
    data = Student.objects.all()
    serializers = StudenSerializer(data,many= True)
    return Response({'playload':serializers.data})


class RegisterUser(APIView):
    def post (self,request ):
        serializer = UserSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()

            user = User.objects.get(username = serializer.data['username'])

            token_obj , created   = Token.objects.get_or_create(user=user)

            return Response({'status': 200, 'token':str(token_obj),'message': serializer.data})
        else:
            return Response({'status': 400, 'message': serializer.errors})


class StudentApis(APIView):

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