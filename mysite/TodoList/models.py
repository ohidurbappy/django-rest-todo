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

