from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


ADMIN = 1
CLIENT = 2


class MyUser(AbstractUser):
    ROLE_CHOICES = (
        (ADMIN, _('Администратор')),
        (CLIENT, _('Пользователь'))
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        default=2,
        verbose_name=_('Роль')
    )

    def __str__(self):
        return f'({self.id}) {self.username}'
