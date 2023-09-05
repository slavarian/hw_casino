from django.core.validators import RegexValidator
from django.db import models

from auths.models.my_user import MyUser


class BankCard(models.Model):
    number = models.CharField(
        verbose_name='номер',
        max_length=16,
        validators=[
            RegexValidator(regex=r'^\d{16}$', message='Number не верный формат')
        ]
    )
    owner = models.OneToOneField(
        verbose_name='пользователь',
        related_name='card',
        to=MyUser,
        on_delete=models.CASCADE
    )
    cvv = models.CharField(
        verbose_name='номер',
        max_length=3,
        validators=[
            RegexValidator(regex=r'^\d{3}$', message='CVV не верный формат')
        ]
    )
    experation_time = models.DateField(
        verbose_name='срок действия'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Банковская карта'
        verbose_name_plural = 'Банковская карты'
