from rest_framework import serializers
from api.models import profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ['id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'rdoc']
         