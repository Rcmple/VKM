from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    isModerator = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'isModerator']

    def get_isModerator(self, obj):
        return obj.groups.filter(name='Moderator').exists()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class AddUserSerializer(serializers.ModelSerializer):
    isModerator = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        self.isModerator = data.get('user').pop('isModerator', False)
        return super().validate(data)


    def to_internal_value(self, data):
        user_data = data.get('user', {})
        return super().to_internal_value(user_data)