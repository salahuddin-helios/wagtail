from .models import Subscriber
from wagtail.contrib.modeladmin.options import (
    modeladmin_register,ModelAdmin
)

class SubscribeAdmin(ModelAdmin):
    model = Subscriber
    menu_label = 'Subscribe'
    menu_icon = 'placeholder'
    list_display = ('email','full_name')
    list_filter = ('email','full_name')
    search_fields = ('email','full_name')

modeladmin_register(SubscribeAdmin)