from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile Database logic."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='User_obj')
    
    profile_img = models.ImageField(
        upload_to='profile_images', 
        default='user.svg', 
        blank=True, 
        null=True, 
        verbose_name='User_pic'
    )

    email_adress = models.CharField(max_length=55, unique=True, null=True, verbose_name='Email')

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    gender = models.CharField(max_length=17, choices=GENDER, blank=True, null=True)

    def __str__(self):
        return self.user.username
