import os

from django.db import models


class Banner(models.Model):
    """banner for Reclama"""
    name = models.CharField(
        verbose_name='баннер',
        max_length=20,
    )
    banner_file = models.ImageField(
        verbose_name='файл баннера',
        upload_to='main',
        default='main/unknown.jpeg')
    
    is_active = models.BooleanField(
        verbose_name='активный',
        default=False,
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'баннер'
        verbose_name_plural = 'баннеры'

    def __str__(self) -> str:
        return self.name
    
    def rename_banner_file(self, filename):
        base_path = 'main/'
        extension = filename.split('.')[-1]
        new_filename = f'{self.name}.{extension}'
        return os.path.join(base_path, new_filename)
