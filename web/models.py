from django.db import models

# Create your models here.


class Award (models.Model):
    award=models.CharField(max_length=50)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.award
    
class Education (models.Model):
    education=models.CharField(max_length=50)
    univercity=models.CharField(max_length=50)

    def __str__(self):
        return self.education

class Experience (models.Model):
    post=models.CharField(max_length=50)
    company=models.CharField(max_length=50)

    def __str__(self):
        return self.post
    

class Work (models.Model):
    workname=models.CharField(max_length=50)
    worktype=models.CharField(max_length=50)
    workimage=models.ImageField()

    def __str__(self):
        return self.workname
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField()
    subject = models.TextField()
    message =models.TextField()
    
   

    def str(self):
        return self.name
    

class  Service (models.Model):
    service_title=models.CharField(max_length=50)
    service_sentence=models.TextField()
    service_icons=models.ImageField()


    def __str__(self):
        return self.service_title
    
class Counter (models.Model):
    countertitle=models.CharField(max_length=50)
    counternumber=models.CharField(max_length=50)
    countericon=models.ImageField()

    def __str__(self):
        return self.countertitle
    


    
    
