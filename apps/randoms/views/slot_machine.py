from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from randoms.models.banner import Banner


class SlotMachineView(View):
    """Класс, который служит для рандомных штук"""

    def get(self, request):
        active_banners = Banner.objects.filter(is_active=True)
        context = {'active_banners': active_banners}
        return render(
            template_name='random/slot_mashine.html',
            request=request,
            context=context
        )
        