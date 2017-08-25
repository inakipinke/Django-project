from django.contrib import admin
from .models import Post
from .models import usuario

admin.site.register(Post)
admin.site.register(usuario)