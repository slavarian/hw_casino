from django.contrib import admin

from randoms.models.banner import Banner
from randoms.models.bet import Bet


class BannerAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'name',
        'is_active',
        'banner_file'
    )
    list_filter: list[str] = (
        'name',
    )   

admin.site.register(Banner, BannerAdmin)
admin.site.register(Bet)