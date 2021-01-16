---
title: Creating a Django REST API
description: Steps to create a very basic django rest api
date: 2021-01-16
tags: 
- python
- django
---

There are a few key options for a REST API request:

- GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide
- POST — Creates a new record that gets appended to the database
- PUT — Looks for a record at the given URI you provide. If it exists, update the existing record. If not, create a new record
- DELETE — Deletes the record at the given URI
- PATCH — Update individual fields of a record



Install Django

```bash
pip install django
```

Install Django REST Framework

```bash
pip install djangorestframework
```

Create a new project

```bash
django-admin startproject mysite
```

crete a new app

```bash
cd mysite
python manage.py startapp TodoList
```

Add the app and the rest framework to the list of installed apps in `settings.py`

```bash
INSTALLED_APPS = [
    'TodoList.apps.TodolistConfig',
    'rest_framework',
    ...
]
```

Run the migrations

```bash
python manage.py migrate
```

Create superuser account

```bash
python manage.py createsuperuser
```

Add the models

```python
from django.db import models

class Group(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
        
class Item(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(default="")
    date=models.DateTimeField()
    completed=models.BooleanField(default=False)
    todo_list=models.ForeignKey(Group,on_delete=models.CASCADE,related_name='items')

    def __str__(self) -> str:
        return self.title

```

Register admin site for TodoList

```python
from .models import Group,Item
admin.site.register(Group)
```

or better

```python

admin.site.index_title="Todo Admin"
admin.site.site_title="Todo Admin"
admin.site.site_header='Welcome to Todo Admin'


from .models import Group,Item
# admin.site.register(Group)

class ItemInline(admin.TabularInline):
    model=Item
    extra=1


class GroupAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['title']}),
    ]

    inlines=[ItemInline]

admin.site.register(Group,GroupAdmin)


```

Make migrations and migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

Create serializers.py

```python
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

```

Create the views

```python
from django.shortcuts import render
from rest_framework import viewsets

from .models import Group,Item
from .serializers import GroupSerializer

# rest api
class GroupViewSets(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('id')
    serializer_class=GroupSerializer

```

Add the urls

```python
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
```

Add the urls to main urls.py

```python
urlpatterns = [
    ...
    path('',include('TodoList.urls')),
]

```