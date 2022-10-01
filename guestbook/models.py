from django.db import models

# Create your models here.
STATUSES = (('active', 'Активно'), ('blocked', 'Заблокировано'))


class GuestBook(models.Model):
    author = models.CharField(verbose_name='Автор', max_length=200, null=False, blank=False)
    email = models.EmailField(verbose_name='Почта', max_length=254, null=False, blank=False)
    text = models.TextField(verbose_name='Текст', max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    status = models.CharField(verbose_name='Статус', max_length=20, null=False, blank=False, choices=STATUSES,
                              default='active')

    def __str__(self):
        return f'{self.author} - {self.status}'
