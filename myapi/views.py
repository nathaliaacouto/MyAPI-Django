from rest_framework import viewsets, generics
from myapi.models import User
from myapi.serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from myapi.utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse 

class UsersViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer

        def post(self, request):
                user = request.data
                serializer = self.serializer_class(data = user)
                user_data = serializer.data
                user = User.objects.get(email = user_data['email'])

                token = RefreshToken.for_user(user).access_token

                current_site = get_current_site(request)
                relativeLink = reverse('email-verify')

                absurl = 'http://' + current_site + relativeLink + '?token='+ str(token)
                email_body = 'Olá, ' + user.nome + 'Clique no link abaixo para verificar seu email\n' + absurl
                data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verifique seu email'}

                Util.send_email(data)

class VerifyEmail(generics.GenericAPIView):
        def get(self):
                pass