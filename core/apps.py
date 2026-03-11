from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.db.models.signals import post_save
        from django.contrib.auth.models import User
        from .models import UserProfile

        def create_owner_profile(sender, instance, created, **kwargs):
            if created and instance.is_superuser:
                UserProfile.objects.get_or_create(user=instance, defaults={'role': 'owner'})

        post_save.connect(create_owner_profile, sender=User)
