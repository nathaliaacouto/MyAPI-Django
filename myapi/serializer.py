from rest_framework import serializers
from myapi.models import User

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ['id', 'nome', 'email']

        def validate(self, attrs):
                email = attrs.get('email', '')
                if User.objects.filter(email = email).exists():
                        raise serializers.ValidationError({'email', ('O e-mail já está sendo utilizado')})
                return super().validate(attrs)