''' RANDOMS URLS'''
from django.urls import path

from randoms.views.base_view import BaseView
from randoms.views.random_view import RandomView
from randoms.views.slot_machine import SlotMachineView


urlpatterns = [
    path('slot_mashine/', SlotMachineView.as_view()),
    path('wheel/', RandomView.as_view(), name='random'),
    path('', BaseView.as_view())
]

# Сделать аналогично с фалом models.py

