from django.contrib import admin

from .models import User_register
from .models import BlogTable
from .models import commenttable

# Register your models here.

admin.site.register(User_register)
admin.site.register(BlogTable)
admin.site.register(commenttable)
