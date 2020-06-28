from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from system.models import UserFavorate

# post_save:接收信号的方式
#sender: 接收信号的model
@receiver(post_save, sender=UserFavorate)
def create_UserFavorate(sender, instance=None, created=False, **kwargs):
    # 是否新建，因为update的时候也会进行post_save
    if created:
        good = instance.good
        good.favorate_num += 1
        good.save()

@receiver(post_delete, sender=UserFavorate)
def delete_UserFavorate(sender, instance=None, created=False, **kwargs):
        good = instance.good
        good.favorate_num -= 1
        good.save()