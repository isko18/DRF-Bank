from rest_framework import serializers
from apps.users.models import Users

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'phone_number', 
                  'created_at', 'age', 'balance')

# class UserDetailSerializers(serializers.ModelSerializer):
#     from_user = 


class RegisterUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(
        max_lenght = 255, write_only=True
    )
    password2 = serializers.CharField(
        max_lenght = 255, write_only=True
    )
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'phone_number',
                   'created_at', 'password', 'password2')
        

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError ({'password2' : 'Пароли различаются'})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError('Номер телефона должна быть в формате +996xxxxxxxx')
        return attrs
    
    def create(self, values):
        user = Users.objects.create(
            username = values['username'], phone_number = values['phone_number'], 
            age = values['age'], email = values['email']
        )
        user.set_password(values['password'])
        user.save()
        return user