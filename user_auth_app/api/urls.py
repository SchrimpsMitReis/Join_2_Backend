from django.urls import include, path
from rest_framework import routers

from user_auth_app.api.views import AccountViewSet, LoginView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = [
    path('', include(router.urls), name='hello_world'),
    path("login/", LoginView.as_view(), name="login"),
]