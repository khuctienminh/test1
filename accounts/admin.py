from django.contrib import admin
from .models import CustomUser


fieldsets = (
        (
            'User profile',
            {
                'fields': (
                    'name',
                    'email',
                    'password',
                    'date_joined',
                    'last_login',
                    'age',
                    'sex',
                    'image',
                )
            }
        )
)

# Register your models here.
admin.site.register(CustomUser)
