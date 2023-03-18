from djongo import models


class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        abstract = False


class crossword(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        abstract = False
