from django.contrib import admin
from zoo.models import Aviary, Animals, Profile


class AviaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']

admin.site.register(Aviary, AviaryAdmin)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
admin.site.register(Animals, AnimalsAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user_id', 'age']

admin.site.register(Profile, ProfileAdmin)