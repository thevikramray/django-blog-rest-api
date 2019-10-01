"""
    1-->ApiView -- path('apiview/', views.HelloApiview.as_view()),

            ----------with rest_framework router---------
    2-->viewsets.Viewset -- routes.register('viewset', views.HelloViewset, base_name='hello-viewset')
            "  BASE NAME TO IDENTIFY AS WE DONT GIVE QUERYSET IN VIEWSET  "

    3-->viewsets.ModelViewset -- routes.register('ModelViewset', views.HelloModelViewset)
            "   NO BASE NAME REQUIRED AS IT WILL BE AUTOMATICALLY GENERATED with the queryset or MODEL or you can overwrite "

"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('profile',views.UserProfileViewset)
router.register('blog',views.UserBlogpostViewset)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]