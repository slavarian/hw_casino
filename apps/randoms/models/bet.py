from django.db import models
from django.db.models.manager import Manager
from django.core.exceptions import ValidationError

from auths.models.my_user import MyUser, Transaction


class BetManager(Manager):
    """
    Model bet's manager
    """

    def create(self, **kwargs: dict) -> 'Bet':
        # Вызывает метод save()
        return super().create(**kwargs)


class Bet(models.Model):
    """
    Bet for game!
    """

    class Games(models.TextChoices):
        WHEEL = (0, 'Колесо фартуны')
        SLOT = (1, 'Игровой Автомат')

    game: str = models.CharField(
        verbose_name='игра',
        max_length=200,
        choices=Games.choices
    )
    amount: float = models.DecimalField(
        verbose_name='сумма',
        max_digits=11,
        decimal_places=2
    )
    who: MyUser = models.ForeignKey(
        verbose_name='кто поставил',
        to=MyUser,
        on_delete=models.CASCADE
    )
    coef: float = models.DecimalField(
        verbose_name='коефицент',
        max_digits=3,
        decimal_places=1
    )

    objects = BetManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'

    def win(self) -> None:
        ...

    def lose(self) -> None:
        ...

    def save(self, *args, **kwargs) -> None:
        Transaction.objects.create(
            user=self.who,
            amout=self.amout
        )
        return super().save(*args, **kwargs)
    
    def clean(self) -> None:
        if self.who.balance <= self.amout:
            raise ValidationError('Не хватает денег!')
        return super().clean()