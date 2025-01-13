from django.contrib.auth.models import User
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class SurveyFormAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.user.username
        email = request.user.email 
        last_login = request.user.last_login

        return Response({
            'username': username,
            'email': email,
            'last_login': last_login
        })