from rest_framework import serializers

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from authentication.models import client, merchant, adminUser
from rest_framework.validators import ValidationError


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        token = Token.objects.create(user=user)

        try:
            if user.is_staff:
                user.groups.add(Group.objects.get(name="admin"))
                admin_name = user.username
                admin = adminUser.objects.create(name=admin_name, user=user)

            else:
                user.groups.add(Group.objects.get(name="client"))
                client_name = user.username
                Client = client.objects.create(name=client_name, user=user)
        except Exception as e:
            user.delete()
            raise ValidationError('Failed to create user')

        return user