from django.db import models
from rest_framework import serializers


from .models import Group, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('id','title','date','completed')



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    items=ItemSerializer(many=True,read_only=True)
    class Meta:
        model=Group
        fields=('id','title','items')
