from django.shortcuts import render
from rest_framework import viewsets


from .models import Group,Item
from .serializers import GroupSerializer

# rest api
class GroupViewSets(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('id')
    serializer_class=GroupSerializer


