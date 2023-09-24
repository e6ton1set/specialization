from django.apps import AppConfig


class BaseBlogAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base_blog_app"
