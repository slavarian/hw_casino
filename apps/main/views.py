"""MAIN APP"""

from django.shortcuts import render
from randoms.models.banner import Banner


def main_page(request):
    active_banners = Banner.objects.filter(is_active=True)
    context = {'active_banners': active_banners}
    return render(
        template_name='new_main.html',
        request=request,
        context = context
    )


# def banner_display(request):
#     active_banners = Banner.objects.filter(is_active=True)
#     return render(request, 'new_main.html', {'active_banners': active_banners})