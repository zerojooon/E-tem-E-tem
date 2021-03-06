from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Powerpoint(models.Model):
    img_src = models.URLField()
    download_link = models.TextField(blank=True, null=True)
    detail_page = models.TextField(blank=True, null=True)
    download_count = models.IntegerField(default =0)

    class Meta:
        db_table = 'pptbizcam_real'


class Cart(models.Model):
    cart_id = models.CharField(max_length=100, blank=True)
    user_num = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    template = models.ForeignKey(Powerpoint, on_delete=models.CASCADE, related_name='template')

    class Meta:
        unique_together = (("template", "cart"),)

    def __str__(self):
        return self.template


class Recent(models.Model):
    user_num = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    recent_id = models.IntegerField(null=True)

    def __str__(self):
        return self.recent_id


class RecentItem(models.Model):
    template_recent = models.ForeignKey(Powerpoint, on_delete=models.CASCADE, related_name='template_recent')
    recent = models.ForeignKey(Recent, on_delete=models.CASCADE)

    def __str__(self):
        return self.template_recent


class DownloadList(models.Model):
    # download_id = models.CharField(max_length=100, blank=True)
    user_id = models.IntegerField(null=True)
    user_num = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user_id


class DownloadItem(models.Model):
    templates = models.ForeignKey(Powerpoint, on_delete=models.CASCADE, related_name='templates')
    download = models.ForeignKey(DownloadList, on_delete=models.CASCADE)

    def __str__(self):
        return self.templates


class ColorTag(models.Model):
    color = models.CharField(max_length=100, db_index=True)


class PPT_tag(models.Model):
    template = models.ForeignKey(Powerpoint, on_delete=models.CASCADE, null=True, related_name='powerpoint')
    ppt_tag = models.ForeignKey(ColorTag, on_delete=models.CASCADE, null=True)


class Myinfo(models.Model):
    pass