from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from JoinApp.api.serializers import AccountSerializer, ContactSerializer, SubtaskSerializer, SummerySerializer, TaskSerializer
from JoinApp.models import Account, Contact, Subtask, Task
from rest_framework import status
from django.db.models import Min, Max


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

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
    
class SummeryView(APIView):

    def get(self, request):
        serializer = SummerySerializer(data=self.combine_data())

        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def combine_data(self):
        sumTask = Task.objects.count()
        latestDealine = self.get_latest_deadline()

        return {
            "sumTask" : sumTask,
            "lateDate": latestDealine,
            "todosCount" : self.get_all_todo(),
            "progressCount" : self.get_all_progress(),
            "feedbackCount" : self.get_all_feedback(),
            "doneCount" : self.get_all_done(),
            "urgendCount" : self.get_all_urgend()
        }

    def get_latest_deadline(self):
        allTasks = Task.objects.aggregate(Max('date'))
        return allTasks['date__max']

    def get_all_todo(self):
        todos = Task.objects.filter(todo = True)
        return todos.count()
    
    def get_all_progress(self):
        progress = Task.objects.filter(progress = True)
        return progress.count()
    
    def get_all_feedback(self):
        feedback = Task.objects.filter(feedback = True)
        return feedback.count()
    
    def get_all_done(self):
        done = Task.objects.filter(done = True)
        return done.count()
    
    def get_all_urgend(self):
        urgend = Task.objects.filter(prio = "Urgent")
        return urgend.count()