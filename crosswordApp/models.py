from djongo import models


class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        abstract = False


class crossword(models.Model):
    # _id = models.ObjectIdField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    width = models.IntegerField()
    height = models.IntegerField()
    creator = models.CharField(max_length=50, default="admin")

    grid= models.CharField(max_length=1000, default="")

    class Meta:
        abstract = False

