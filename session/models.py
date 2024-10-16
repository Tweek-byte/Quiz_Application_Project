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
    def profile_img_url(self):
        if self.profile_img and self.profile_img.name != '':
            return self.profile_img.url
        return '/static/images/user.svg'

    email_address = models.CharField(max_length=55, unique=True, null=True, verbose_name='Email')

    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Age')
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    gender = models.CharField(max_length=17, choices=GENDER, blank=True, null=True)

    def __str__(self):
        return self.user.username
