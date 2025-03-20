from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework import status

from django.contrib.auth.hashers import check_password
from user_auth_app.api.serializers import AccountSerializer
from user_auth_app.models import Account
from rest_framework.permissions import AllowAny, IsAuthenticated

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]  # Jeder darf einen Account erstellen
        return [IsAuthenticated()] 

class LoginView(APIView):
    authentication_classes = []
    permission_classes = [] 
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return Response({"error": "User Existiert nicht"}, status=status.HTTP_404_NOT_FOUND)
        
        if not check_password(password, user.password):
            return Response({"error": "Ungültige Anmeldeinformationen"}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "user_id": user.id}, status=status.HTTP_200_OK)
