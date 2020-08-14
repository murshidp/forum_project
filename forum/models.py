from django.db import models

# Create your models here.


class Forum(models.Model):
    master = models.CharField(max_length=150)

    def __str__(self):
        return self.master

class Subforum(models.Model):
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(max_length=150)
    forum_category=models.ForeignKey(Subforum,on_delete=models.CASCADE)
    description = models.TextField()
    haederimage=models.ImageField()