from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=11)
    problem = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"

