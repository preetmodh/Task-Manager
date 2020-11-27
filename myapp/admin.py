from django.contrib import admin
from .models import User,Content
# Register your models here.

admin.site.register(User)
admin.site.register(Content)
#<!-- background-image:url( "{% static 'images\backg.png' %}")-->