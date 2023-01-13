from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=20)
    email=models.CharField(max_length=120)
    message=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name

class magazines(models.Model):
    name=models.CharField(max_length=150)
    mpic=models.ImageField(upload_to='static/magazines',default="")
    mdate=models.DateField()
    mfile=models.FileField(upload_to='static/magazines',default="")

    def __str__(self):
        return self.name

class front(models.Model):
     name=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/magazines',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     pfile=models.FileField(upload_to='static/magazines',default="")

     def __str__(self):
         return self.name


class category(models.Model):
    cname=models.CharField(max_length=100)
    cpic=models.ImageField(upload_to='static/computercat/',default="")
    cdate=models.DateField()

    def __str__(self):
        return self.cname

class computerscience(models.Model):
     name=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/computerscience',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/computerscience',default="")

     def __str__(self):
         return self.name

class mechanicalautomobile(models.Model):
     name=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/mechanicalautomobile',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/mechanicalautomobile',default="")

     def __str__(self):
         return self.name

class mechanicalproduction(models.Model):
     name=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/mechanicalproduction',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/mechanicalproduction',default="")

     def __str__(self):
         return self.name

class electronics(models.Model):
     name=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/electronics',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/electronics',default="")

     def __str__(self):
         return self.name

class image(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='static/gallery',default="")

    def __str__(self):
        return self.name

### Notes section start Here...##

class csnote(models.Model):
     subject=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/csnotes',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/csnotes',default="")

     def __str__(self):
         return self.subject

class manote(models.Model):
     subject=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/manotes',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/manotes',default="")

     def __str__(self):
         return self.subject

class eenote(models.Model):
     subject=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/eenotes',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/eenotes',default="")

     def __str__(self):
         return self.subject

class mpnote(models.Model):
     subject=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/mpnotes',default="")
     branch=models.CharField(max_length=150)
     lan=models.CharField(max_length=50)
     pdate=models.DateField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/mpnotes',default="")

     def __str__(self):
         return self.subject


### previous year peper  model start here...##

class csqp(models.Model):
     subject=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/csqp',default="")
     branch=models.CharField(max_length=150)
     year=models.IntegerField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/csqp',default="")

     def __str__(self):
         return self.subject

class maqp(models.Model):
     subject=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/maqp',default="")
     branch=models.CharField(max_length=150)
     year=models.IntegerField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/maqp',default="")

     def __str__(self):
         return self.subject

class eeqp(models.Model):
     subject=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/eeqp',default="")
     branch=models.CharField(max_length=150)
     year=models.IntegerField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/eeqp',default="")

     def __str__(self):
         return self.subject

class mpqp(models.Model):
     subject=models.CharField(max_length=150)
     ppic=models.ImageField(upload_to='static/mpqp',default="")
     branch=models.CharField(max_length=150)
     year=models.IntegerField()
     sem=models.ForeignKey(category,on_delete=models.CASCADE)
     pfile=models.FileField(upload_to='static/mpqp',default="")

     def __str__(self):
         return self.subject