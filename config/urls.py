from django.contrib import admin
from django.urls import path, include
from myapi.views import UsersViewSet, VerifyEmail
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('email-verify/', VerifyEmail.as_view(), name = 'email-verify')
]
