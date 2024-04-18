from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password1'])
        user.save()

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=20, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs



class UserUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    phone = serializers.CharField(max_length=15, required=False)
    password = serializers.CharField(max_length=128, write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'phone', 'password']

    def validate(self, attrs):
        user = self.instance  # Get the user instance
        if 'password' in attrs:
            user.set_password(attrs['password'])  # Set new password if provided
            user.save()
        return attrs