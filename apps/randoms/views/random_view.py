'''RANDOM VIEWS'''
import random


from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from randoms.models.banner import Banner


class RandomView(View):
    """Класс, который служит для рандомных штук"""

    def get(self, request):
        random_number = random.randint(-100, 100)
        active_banners = Banner.objects.filter(is_active=True)
        context = {'random_number': random_number,
                   'active_banners': active_banners}
        return render(
            template_name='random/wheel.html',
            request=request,
            context = context
        )
    