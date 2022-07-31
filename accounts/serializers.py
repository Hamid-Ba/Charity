from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ("username","password","phone","address","gender","age","description",
        'first_name','last_name','email')
        write_only_fields = ('password',)

    def create(self,validate_data):
        user = User.objects.create(
            username = validate_data['username'],
            phone = validate_data['phone'],
            address = validate_data['address'],
            gender = validate_data['gender'],
            age = validate_data['age'],
            description = validate_data['description'],
            first_name = validate_data['first_name'],
            last_name = validate_data['last_name'],
            email = validate_data['email'],
        )

        user.set_password(validate_data['password']) 
        user.save()
        return user