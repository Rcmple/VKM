from django.contrib.auth.models import User, Group
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
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'isModerator']
        extra_kwargs = {'password': {'write_only': True}}

    def to_internal_value(self, data):
        user_data = data.get('user', {})
        return super().to_internal_value(user_data)

    def create(self, validated_data):
        is_moderator = validated_data.pop('isModerator', False)
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        if is_moderator:
            user.groups.add(Group.objects.get(name='Moderator'))
        return user
