from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'zip_code')

    password = serializers.CharField(
            min_length=8,
            max_length=128,
            )
    
    def create(self, validated_data):
        u =  User.objects.create(**validated_data)
        u.set_password(validated_data.get('password'))
        return u
