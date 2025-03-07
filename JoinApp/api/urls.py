from django.urls import include, path
from .views import AccountViewSet, ContactsViewSet, LoginView, SubtaskViewSet, SummeryView, TasksViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactsViewSet)
router.register(r'tasks', TasksViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls), name='hello_world'),
    path("login/", LoginView.as_view(), name="login"),
    path("summery/", SummeryView.as_view(), name="summery"),
    # path('contacts/', hello_world, name='hello_world'),
]