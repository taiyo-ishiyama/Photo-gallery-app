from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    # category
    title = models.CharField(
        verbose_name='category',
        max_length=20)
    
    def __str__(self):
        return self.title

class PhotoPost(models.Model):
    '''manage posted data
    '''
    # custom user: parent, PhotoPost: child
    user = models.ForeignKey(
        CustomUser,
        verbose_name='user',
        # For deletion, removing all user data
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Category,
        verbose_name='category',
        # Ensure not to delete the category
        on_delete=models.PROTECT
        )
    title = models.CharField(
        verbose_name='title',
        max_length=200
        )
    comment = models.TextField(
        verbose_name='comment',
        )
    image1 = models.ImageField(
        verbose_name='image1',
        upload_to = 'photos'
        )
    image2 = models.ImageField(
        verbose_name='image2',
        upload_to = 'photos',
        blank=True,
        null=True
        )
    posted_at = models.DateTimeField(
        verbose_name='Posted date',
        auto_now_add=True
        )
    
    def __str__(self):
        return self.title
