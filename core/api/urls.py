from home.views import *
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('index/',index),
    path('student/',StudentApis.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterUser.as_view()),
    path('api-token-auth/', views.obtain_auth_token)
    # path('update/<id>',update_student)
    
]