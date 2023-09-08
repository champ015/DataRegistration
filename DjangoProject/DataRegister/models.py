from django.db import models
class position(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class employee(models.Model):
    Name=models.CharField(max_length=50)
    EmpCode=models.CharField(max_length=50)
    Mobiel_No=models.CharField(max_length=50)
    Position=models.ForeignKey(position,on_delete=models.CASCADE)

# Create your models here.
