from django.db import models
 
# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    A1 = models.CharField(max_length=200,null=True)
    A2 = models.CharField(max_length=200,null=True)
    A3 = models.CharField(max_length=200,null=True)
    A4 = models.CharField(max_length=200,null=True)
    A5 = models.CharField(max_length=200,null=True)
    
    
    def __str__(self):
        return self.question

class UserModel(models.Model):
    userName = models.CharField(max_length=30, null=False)
    userEmail = models.CharField(max_length=60, null=False)
    userPassword = models.CharField(max_length=25, null=False)