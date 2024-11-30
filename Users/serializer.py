from rest_framework import serializers


class SignUpInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    birthDate = serializers.DateField(source="birth_date")

    class Meta:
        abstract = True


class SignUpOutputSerializer(SignUpInputSerializer):
    password = None
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")


class LogInInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)


class LogInOutputSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")
