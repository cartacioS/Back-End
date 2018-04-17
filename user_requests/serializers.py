from .models import UserRequests
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):

    poster = serializers.PrimaryKeyRelatedField(read_only = True, default = serializers.CurrentUserDefault())
    class Meta:
        model = UserRequests
        fields = ('title', 'poster', 'expiration_date', 'group_size', 'members_needed', 'description')

    
    def create(self, validated_data):
        u =  UserRequests.objects.create(**validated_data)
        u.save()
        return u
