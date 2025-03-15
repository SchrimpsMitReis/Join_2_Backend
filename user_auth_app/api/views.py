from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework import status

from django.contrib.auth.hashers import check_password
from user_auth_app.api.serializers import AccountSerializer
from user_auth_app.models import Account

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return Response({"error": "Ungültige Anmeldeinformationen"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not check_password(password, user.password):
            return Response({"error": "Ungültige Anmeldeinformationen"}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "user_id": user.id}, status=status.HTTP_200_OK)
