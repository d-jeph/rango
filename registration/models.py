from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    #link user profile to to a User model instance
    user = models.OneToOneField(User)

    # The additional attributes to the user models
    website = models.URLField(blank=True) #to hold the user's link to their website
    picture = models.ImageField(upload_to='profile_images', blank=True) #to hold their profile Image

    # Override the __unicode__() method to return the username
    def __str__(self):
        return self.user.username
