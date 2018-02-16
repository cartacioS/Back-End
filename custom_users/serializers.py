from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
            min_length=8,
            max_length=128,
            write_only=True
            )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'zip_code')
        extra_kwargs = { 'password' : { 'write_only' : True } }

    
    def create(self, validated_data):
        u =  User.objects.create(**validated_data)
        u.set_password(validated_data.get('password'))
        u.save()
        return u
