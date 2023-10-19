from django.db import models

# Create your models here.


class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    heading_post = models.CharField(max_length=1000)
    content_heading_post = models.CharField(max_length=5000, default='')

    heading = models.CharField(max_length=500)
    content_heading = models.CharField(max_length=500, default='')

    sub_heading = models.CharField(max_length=500)
    content_sub_heading = models.CharField(max_length=500, default='')

    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.title
