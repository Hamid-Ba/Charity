from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ("username","password","phone","address","gender","age","description",
        'first_name','last_name','email')
        write_only_fields = ('password',)

    def create(self,validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password']) 
        user.save()
        return user