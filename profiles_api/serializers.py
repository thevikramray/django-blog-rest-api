# In ModelSerilizer Default `.create()` and `.update()` implementations are provided.  


from rest_framework import serializers
from profiles_api import models

class ProfileUserSerilizer(serializers.ModelSerializer):
    """ ModelSerilizer  for handling new users. It is 
        similar to serilizerals.Serilizer except it pre-populate and 
        add Default Validator """

    class Meta:
        model = models.ProfileUser
        fields = ('id','email','first_name','last_name','password')
        extra_kwargs = {
            'password': {
                 'write_only': True,
                 'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ OverWriting default 'create' to use create_user to create a new user
            and save hashed password and return a new Profile User """

        user = ProfileUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )
        return user



    # 'write_only': False          in password
    #     {
    #         "id": 8,
    #         "email": "vikram2@gmail.coms",
    #         "first_name": "vikram",
    #         "last_name": "",
    #         "password": "pbkdf2_sha256$150000$2gzZ4iBHC2JO$JoEFFnQF+VC7q0tUk3WVry21LuBaUqzMHyB0GMenUwU="
    #     }
    
    # 'write_only': True            in password
    #     {
    #         "id": 8,
    #         "email": "vikram2@gmail.coms",
    #         "first_name": "vikram",
    #         "last_name": "",
    #     }

    # write-only = True ----> Only POST
    # read-only = True ----> Only GET

class BlogpostSerilizer(serializers.ModelSerializer):
    """ Serilizer for validation of Blogpost data """
    class Meta:
        model = models.UserBlogpostModel
        fields = ('id','created_by','created_at','title','content')
        extra_kwargs = {
            'created_by':{'read_only':True}
        }

"""
    As currently implemented, setting auto_now or auto_now_add to True will cause the field to have 
    editable=False and blank=True set.
"""