from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    desc= models.TextField()
    date = models.DateField()




    def __str__(self):
        return 'Message from  ' +self.name 






"""
    def __str__(self):
        return 'Message from  ' +self.name + ' - '  +self.email 

        # you can used this also but print name and email both       
"""
     

     

     