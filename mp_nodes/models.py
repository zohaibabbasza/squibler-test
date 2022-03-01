from django.db import models
from django.contrib.auth.models import User
from treebeard.mp_tree import MP_Node

class TreeSection(MP_Node):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mp_owner", null=True
    )
    collaboration = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return self.title + " | " + self.owner.email
