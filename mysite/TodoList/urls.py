from django.urls import path,include
from rest_framework import routers
import rest_framework

from . import views

router=routers.DefaultRouter()
router.register(r'groups',views.GroupViewSets)

urlpatterns=[
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]