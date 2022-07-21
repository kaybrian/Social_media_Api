from .models import User 
from rest_framework import serializers 
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    email = serializers.EmailField(max_length=60)
    phone_number = PhoneNumberField(allow_null=False,allow_blank=False)
    password = serializers.CharField(min_length=8,write_only=True)


    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','phone_number','password']

    def validate(self, attrs):
        username_exits = User.objects.filter(username=attrs['username']).exists()

        if username_exits:
            raise serializers.ValidationError(detail="User with username exists")

        email_exits = User.objects.filter(email=attrs['email']).exists()

        if email_exits:
            raise serializers.ValidationError(detail="A user with the same email Exits")

        phone_number_exits = User.objects.filter(phone_number=attrs['phone_number']).exists()

        if phone_number_exits:
            raise serializers.ValidationError(detail="A user with the same phone number Exits")

        return super().validate(attrs)

        
    def create(self, validated_data):
        user = User.objects.create(
         username = validated_data['username'],
         first_name=validated_data['first_name'],
         last_name=validated_data['last_name'],
         email = validated_data['email'],
         phone_number = validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user