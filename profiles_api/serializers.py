from rest_framework import serializers
from profiles_api.models import ProfileUser

class ProfileUserSerilizer(serializers.ModelSerializer):
    """ ModelSerilizer  for handling new users. It is 
        similar to serilizerals.Serilizer except it pre-populate and 
        add Default Validator """

    class Meta:
        model = ProfileUser
        fields = ('id','email','first_name','last_name','password')
        extra_kwargs = {
            'password': {
                 'write_only': True,
                 'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ OverWriting default create to use create_user to create a new user
            and save hashed password and return a new Profile User """

        user = ProfileUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )
        return user
