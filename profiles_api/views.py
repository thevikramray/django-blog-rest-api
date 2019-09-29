from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

"""
    ObtainAuthToken.renderer_classes = (renderers.JSONRenderer,) --> 
        rest_framework.renderers
        Renderers are used to serialize a response into specific media types.
        They give us a generic way of being able to handle various media types on the response, such as JSON encoded data or HTML output.
        REST framework also provides an HTML renderer that renders the browsable API.
"""

from rest_framework.authtoken.views import ObtainAuthToken
"""
    A settings object, that allows API settings to be accessed as properties. For example:
        from rest_framework.settings import api_settings  
        print(api_settings.DEFAULT_RENDERER_CLASSES)  
    Any setting with string import paths will be automatically resolved and return the class, rather than the string literal.

"""
from rest_framework.settings import api_settings

from profiles_api import models, serializers
from profiles_api.permissions import UpdateOwnProfile

"""
    rest_framework.views.ApiView we have to define (get, post, put, patch, delete)
    rest_framework.viewsets.Viewset is slightly advance that doesnt provide any action by default.
        but we 'CAN' define (list, create, retreive, update, partial-update)
    rest_framework.viewsets.ModelViewSet is advance that by default give us access to 
        (list, create, retreive, update, partial-update) as we give "queryset=YOURMODEL.queryset.all()"

        -----------------serilizer_class in all 3---------------
"""




class UserProfileViewset(viewsets.ModelViewSet):
    """ Viewset to handle Users"""

    serializer_class = serializers.ProfileUserSerilizer
    queryset = models.ProfileUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    """
        Provides generic filtering backends that can be used to filter the results
        returned by list views.
    """
    filter_backends = (filters.SearchFilter,)    # The URL query parameter used for the search.
    search_fields = ('first_name', 'last_name', 'email',)




class UserLoginApiView(ObtainAuthToken):
    """create auth token for users"""

    """'    
        -----ObtainAuthToken view doesNot have renderer class as as other viewset ---
        DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
            ),
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class UserBlogpostViewset(viewsets.ModelViewSet):
    """ Handle views for posts """
    serializer_class = serializers.BlogpostSerilizer
    queryset = models.UserBlogpostModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    