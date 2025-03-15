from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from JoinApp.models import Contact, Subtask, Task
# from JoinApp.models import Account
# from django.contrib.auth.hashers import make_password


class ContactSerializer(serializers.ModelSerializer):
    tel = PhoneNumberField(region="DE")
    class Meta:
        model = Contact
        fields = "__all__"

class SubtaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subtask
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)

# class AccountSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(write_only=True, required=True)

#     class Meta(ContactSerializer.Meta):
#         model = Account
#         fields = ["id", "name", "email", "tel", "password"]

#     def create(self, validated_data):
#         validated_data["password"] = make_password(validated_data["password"])  # Passwort hashen
#         return super().create(validated_data)   
    
#     def update(self, instance, validated_data):
#         if "password" in validated_data:
#             validated_data["password"] = make_password(validated_data["password"])
#         return super().update(instance, validated_data)

class TaskSerializer(serializers.ModelSerializer):

    worker = ContactSerializer(many=True, read_only=True)

    worker_ids = serializers.PrimaryKeyRelatedField(
        queryset = Contact.objects.all(),
        many = True,
        write_only = True,
        source = 'worker'
    )

    subtasks = SubtaskSerializer(many=True, read_only=True)

    subtask_ids = serializers.PrimaryKeyRelatedField(
        queryset = Subtask.objects.all(),
        many = True,
        write_only = True,
        source = 'subtasks',
        required = False
    )

    class Meta:
        model = Task
        fields = "__all__"



class SummerySerializer(serializers.Serializer):
    sumTask = serializers.IntegerField()
    lateDate = serializers.DateField(allow_null = True)
    todosCount = serializers.IntegerField()
    progressCount = serializers.IntegerField()
    feedbackCount = serializers.IntegerField()
    doneCount = serializers.IntegerField()
    urgendCount = serializers.IntegerField()
