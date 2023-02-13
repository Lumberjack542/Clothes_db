from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Shoes, Wardrobe
# Register your models here.
class WardrobeAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_image']
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width=50 height=60>')

admin.site.register(Shoes)
admin.site.register(Wardrobe, WardrobeAdmin)


