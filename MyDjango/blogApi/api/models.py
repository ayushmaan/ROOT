from django.db import models

from django.contrib.auth.models import User



class Books(models.Model):

    BookName = models.CharField(max_length=100, null=False,unique=True)
    WhoUpdated = models.ForeignKey(User)
    Author = models.CharField(max_length=50,null=False,default="Unknown")
    Pages  = models.IntegerField(null=False)
    NoOfReader = models.IntegerField(null=True)
    Updated = models.DateTimeField(auto_now=True,auto_now_add=False)






    def __str__(self):
        return self.BookName




# Create your models here.
