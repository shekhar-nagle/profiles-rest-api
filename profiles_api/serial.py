from rest_framework import serializers
from profiles_api import models
class HelloSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    age = serializers.IntegerField()


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a user profile object """
    """ Note: Define a meta class , the way you work with ModelSerializer is to use a meta class to configure
    a serializer to point to a specific model in our project. Class Meta will point to UserProfile models
    .Here need to specify list of fields in our model that has to manage through serializer """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email','name', 'password')
        extra_kwargs = {
        'password' : { 'write_only' : True, 'style' :{'input_type' :'password'}}
        }

    """Now override the create function of DRF so as to save password in hash type not in simple readable format"""

    """Whenever we create a profile object with our serializer. It will validate the object and
    fields, provided to serializer and then it will call the create function and passing it in validated_data"""
    def create(self, validated_data):
        """create and return new user"""
        user = models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        )
        return user
        """Note: it will override the create function and call our create_user function from models.py file."""

    def update(self, instance, validated_data):
        """Handle update user account """
        if 'password' in validated_data:
            password=validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
    """The default update logic for DRF ModelSerializer will take whatever fields are
    provided(in our case name, email and password) and pass them directly to the model.
    This is fine with the fields like name and email, However the password field require some additional logic
    to hash the pasword before saving the update. Now password will be save in hash or non readable form.
    Therefore we override the update() method to add this logic to check the presence of password in validated_data
    which is passed from DRF when updating an object.
    If the fields exists we will pop the password from the validated_data dictionary and set it using set_password
    which is save the password in Hash type.
    Once that done we use super().update() to pass the values to the existing DRF update method,
    to handle the remaining fields"""
