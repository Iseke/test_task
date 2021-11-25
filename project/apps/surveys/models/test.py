from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    question = models.CharField(
        max_length=255,
        verbose_name=_('Вопрос')
    )
    survey = models.ForeignKey(
        to='Survey',
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name=_('Опрос'),
        blank=True
    )

    def __str__(self):
        return f'{self.question},  {self.survey}'


class Answer(models.Model):
    answer = models.CharField(
        max_length=128,
        verbose_name=_('Ответ')
    )
    is_correct = models.BooleanField(
        default=False,
        verbose_name=_('Это правильно')
    )
    question = models.ForeignKey(
        to='Question',
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name=_('Вопрос')
    )
    
    def __str__(self):
        return f'{self.answer}  -  {self.is_correct}'
