from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email', 'username', 'password', 'bookmarked_projects']
        id = serializers.ReadOnlyField()
        username = serializers.CharField(max_length=200)
        email = serializers.CharField(max_length=200)
        extra_kwargs = {'password': {'write_only': True}}
        bookmarked_projects = serializers.ReadOnlyField()

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    old_password = serializers.CharField(write_only=True, required=True)
    success = serializers.BooleanField(read_only=True, default=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'username', 'success')
        read_only_fields = [
            'username'
        ]


    def validate_old_password(self, value):
        instance = getattr(self, "instance", None)
        # print(f"{instance=} {value=}")
        if not instance: 
            raise serializers.ValidationError({"old_password": "Instance not found"})
        
        # print(instance.check_password(value))

        if not instance.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance