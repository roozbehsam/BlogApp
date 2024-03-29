from django.apps import AppConfig


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog.post'
    label = "blog_post"
