from django.contrib import admin

# Register your models here.
from crosswordApp.models import user, crossword

admin.site.register(user)
admin.site.register(crossword)
