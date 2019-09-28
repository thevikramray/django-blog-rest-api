from django.shortcuts import render
from rest_framework import viewsets

from profiles_api import models, serializers

"""
    rest_framework.views.ApiView we have to define (get, post, put, patch, delete)
    rest_framework.viewsets.Viewset is slightly advance that doesnt provide any action by default.
        but we 'CAN' define (list, create, retreive, update, partial-update)
    rest_framework.viewsets.ModelViewSet is advance that by default give us access to 
        (list, create, retreive, update, partial-update) as we give "queryset=YOURMODEL.queryset.all()"

        -----------------serilizer_class in all 3---------------
"""

class UserProfileView(viewsets.ModelViewSet):
    """ Viewset to handle users"""

    serializer_class = serializers.ProfileUserSerilizer
    queryset = models.ProfileUser.objects.all()
