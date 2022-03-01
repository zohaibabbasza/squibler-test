from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        blank=True,
        related_name="subsection",
    )
    created_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner", null=True
    )
    collaboration = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return self.title + " | " + self.owner.email
