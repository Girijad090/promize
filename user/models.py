from django.db import models

# Create your models here.
class UserRegister(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone_no = models.CharField(max_length = 10)

    def __str__(self):
        return self.first_name + self.last_name