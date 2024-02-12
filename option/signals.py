from django.db.models.signals import post_save
from django.dispatch import receiver
from option.models import PostOption


@receiver(post_save, sender=PostOption)
def post_save__post_option(sender, instance, created, **kwargs):
    instance.post.json = instance.post.make_json_fields()
    instance.post.save()
    print("post_save__post_option")
